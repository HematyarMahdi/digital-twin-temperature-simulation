import numpy as np
import matplotlib.pyplot as plt
import time

class Room:

    def __init__(self, initial_temp, outside_temp, heater_power):   # This is the initializer method. It sets up the initial state of the room.
        self.temp = initial_temp    # Sets the initial temperature of the room.
        self.outside_temp = outside_temp    # Sets the outside temperature.
        self.heater_power = heater_power    # Sets how much the heater can increase the temperature.

    def update_temperature(self, heater_on, dt=1):    # This method updates the room’s temperature.
        if heater_on:   # Checks if the heater is on.
            self.temp += self.heater_power * dt     #  If the heater is on, the temperature increases.
        else:   # If the heater is off:
            self.temp -= (self.temp - self.outside_temp) * 0.1 * dt     # The temperature cools down towards the outside temperature.
        return self.temp    # Returns the updated temperature.

class DigitalTwin:  # This defines a blueprint for creating a DigitalTwin object that mirrors the room.
    def __init__(self, initial_temp, outside_temp, heater_power):   # his initializes the digital twin with the same starting conditions as the room.
        self.simulated_temp = initial_temp  # Sets the initial temperature of the digital twin.
        self.outside_temp = outside_temp        # Sets the outside temperature.
        self.heater_power = heater_power        # Sets the power of the heater in the digital twin.

    def update_state(self, real_temp):      # This method updates the digital twin’s temperature to match the real room’s temperature.
        self.simulated_temp = real_temp     # The digital twin’s temperature is set to the real room’s temperature.

    def predict_temperature(self, heater_on, dt=1, steps=10):   # This method predicts future temperatures for the next few steps.
        heater_effect = self.heater_power * dt  # Calculates how much the heater would increase the temperature per step.
        cooling_effect = lambda temp: (temp - self.outside_temp) * 0.1 * dt     # Calculates how much the temperature would drop per step if the heater is off.
        
        temps = np.full(steps, self.simulated_temp) # Creates an array to store predicted temperatures, all starting with the current simulated temperature.
        for i in range(steps):  # This loop goes through each future step to calculate the temperature.
            if heater_on:   # Checks if the heater is on.
                temps[i] += heater_effect   # Increases the temperature if the heater is on.
            else:   # If the heater is off:
                temps[i] -= cooling_effect(temps[i])    # Decreases the temperature.
        return temps    # Returns the array of predicted temperatures.

# Initial conditions
initial_temp = 20  # Initial room temperature       Sets the initial temperature of the room and digital twin to 20°C.
outside_temp = 5   # Outside temperature            Sets the outside temperature to 5°C.
heater_power = 1   # Heater's power (temperature change per time unit)      The heater can increase the temperature by 1°C per time unit.

# Create room and digital twin
room = Room(initial_temp, outside_temp, heater_power)   # Creates a Room object with the initial settings.
digital_twin = DigitalTwin(initial_temp, outside_temp, heater_power)    # Creates a DigitalTwin object with the same initial settings.

# Simulation parameters
time_steps = 50     # The simulation will run for 50 time steps.
# Creates an array where the heater is on (1) for the first 25 steps and off (0) for the last 25 steps.
heater_schedule = np.array([1 if t < 25 else 0 for t in range(time_steps)])  # Heater on for the first half     

# Real-time simulation and digital twin prediction
real_temps = []     # An empty list to store the actual temperatures of the room.
predicted_temps = []       # An empty list to store the predicted temperatures from the digital twin.

plt.ion()  # Turn on interactive mode for real-time plotting
# Turns on interactive mode in matplotlib, allowing real-time updates of the plot.

for t in range(time_steps):
    # Simulate real-time temperature update
    real_temp = room.update_temperature(heater_schedule[t]) # Updates the room's temperature based on whether the heater is on or off.
    real_temps.append(real_temp)    # Adds the updated temperature to the real_temps list.

    # Update Digital Twin with the real temperature
    digital_twin.update_state(real_temp)    # Updates the digital twin’s temperature to match the real room's current temperature.

    # Predict future temperature using Digital Twin
    predicted_temp = digital_twin.predict_temperature(heater_schedule[t], steps=1)[0]   # Predicts the next temperature based on the current state.
    # steps=1 means we are predicting just one step ahead.
    # [0] gets the first (and only) predicted value.
    predicted_temps.append(predicted_temp)  # Adds this prediction to the predicted_temps list.

    # Real-time plotting
    plt.clf()   # Clears the current plot so we can draw the new data.
    plt.plot(real_temps, label='Real Temperature')  # Plots the actual temperatures.
    plt.plot(predicted_temps, label='Predicted Temperature', linestyle='--')    # Plots the predicted temperatures with a dashed line.
    plt.xlabel('Time Step') # Labels the x-axis as "Time Step."
    plt.ylabel('Temperature (°C)')  # Labels the y-axis as "Temperature (°C)."
    plt.title('Digital Twin Temperature Simulation (Real-Time)')    # Sets the title of the plot.
    plt.legend()    # Adds a legend to the plot to differentiate between the real and predicted temperatures.
    plt.pause(0.1)  # Pauses for a short time to allow the plot to update.
    time.sleep(0.1)  # Simulates a delay, making the simulation feel like it's happening in real-time.

plt.ioff()  # Turns off interactive mode after the loop ends.
plt.show()  # Displays the final plot with all the collected data.
