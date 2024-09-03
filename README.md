# Real-Time Digital Twin Temperature Simulation

Project Overview

This project demonstrates a basic implementation of a Digital Twin for simulating and predicting the temperature inside a room in real-time. A Digital Twin is a virtual model of a physical system that mirrors its behavior and conditions. In this project, we create a Digital Twin that tracks and predicts the temperature of a room based on whether the heater is on or off.

How It Works

  - Room Model: We simulate a physical room where the temperature can be influenced by an outside environment and a heater.
  - Digital Twin: This is a virtual copy of the room. It receives real-time temperature data from the simulated room and uses this information to predict future temperatures.
  - Real-Time Simulation: The program runs in a loop to mimic real-time data collection, updating the room’s temperature and adjusting the Digital Twin accordingly. The Digital Twin then predicts what the temperature will be in the next moment.
  - Visualization: The actual and predicted temperatures are plotted in real-time, allowing you to see how well the Digital Twin's predictions match the real room's temperature.

Key Components

  - Room Class: Simulates the actual room environment. It updates the temperature based on the heater's status and the outside temperature.
  - Digital Twin Class: Mirrors the room's behavior. It updates its state based on real-time data from the room and predicts future temperatures.
  - Real-Time Plotting: Displays the real and predicted temperatures on a graph that updates in real-time as the simulation progresses.

Technologies Used

  - Python: The core programming language used to build the simulation.
  - NumPy: For efficient numerical operations, especially handling arrays.
  - Matplotlib: For real-time plotting of temperature data.

How to Run the Project

1. Clone the Repository:
```
git clone https://github.com/HematyarMahdi/digital-twin-temperature-simulation.git
cd digital-twin-temperature-simulation
```
2. Install Dependencies: Make sure you have Python installed, then install the required libraries:
```
pip install numpy matplotlib
```
3. Run the Simulation: Simply run the Python script:
```
python digital_twin_simulation.py
```

Watch the real-time plot of the room's temperature and the Digital Twin's predictions.
