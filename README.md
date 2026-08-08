# AI-Assignment

# CSC3206 Artificial Intelligence - Assignment 2
## House Visit Tour - A* Search Implementation

### Overview
This folder contains the Python implementation of the A* Search algorithm designed to solve the House Visit Tour problem. The program calculates the optimal route starting from Sunway University and visiting the residential locations of all five group members (Subang Jaya, Puchong, Shah Alam, Petaling Jaya, and Klang) while minimizing the total driving time. 

The path costs (edge weights) are based on estimated travel times in minutes collected from Google Maps under normal driving conditions.

### Prerequisites
*   **Python 3.x** must be installed on your system.
*   **No external libraries** (such as NumPy or Pandas) are required. The script relies entirely on standard built-in Python libraries, specifically the `heapq` module for managing the priority queue.

### Files Included
*   `AI_Assignment_2.py`: The main Python script containing the graph data, heuristic function, A* search logic, and execution block.
*   `README.md`: This instruction file.

### Execution Instructions
To execute the code and view the results, follow these steps:

1.  Open your Terminal (macOS/Linux) or Command Prompt / PowerShell (Windows).
2.  Navigate to the directory where the unzipped files are located using the `cd` command.
    ```bash
    cd path/to/assignment_folder
    ```
3.  Run the Python script by executing the following command:
    ```bash
    python AI_Assignment_2.py
    ```
    *(Note: Depending on your system configuration, you may need to use `python3 astar_tour.py`)*

### Expected Output
Upon successful execution, the terminal will output the optimal step-by-step path determined by the A* Search algorithm, followed by the total estimated travel time in minutes. 

The output will look similar to this format:
```text

A* Search for the House Visit Tour...

Step-by-Step Path:
  0. Sunway University
  1. [Next Location]
  2. [Next Location]
  ...

Total Estimated Travel Time: [X] minutes
