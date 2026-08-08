# CSC3206 Artificial Intelligence - Assignment 2
## House Visit Tour - A* Search Implementation

### Overview
This folder contains the Python implementation of the A* Search algorithm designed to solve the House Visit Tour problem[cite: 10]. The program calculates the optimal route starting from Sunway University and visiting the residential locations of all five group members (Subang Jaya, Puchong, Shah Alam, Petaling Jaya, and Klang) while minimizing the total driving time[cite: 10]. 

The path costs (edge weights) are based on estimated travel times in minutes collected from Google Maps under normal driving conditions[cite: 9, 10]. Additionally, a visualization script is provided to generate a graphical representation of the final computed route.

### Prerequisites
*   **Python 3.x** must be installed on your system[cite: 10].
*   **Matplotlib:** While the core search algorithm uses only standard built-in libraries like `heapq`[cite: 9, 10], the supplementary visualization script requires the `matplotlib` library. 

To install the required visualization library, run the following command in your terminal:
`pip install matplotlib`

### Files Included
*   `AI_Assignment_2.py`: The main Python script containing the graph data, heuristic function, A* search logic, and execution block[cite: 9, 10].
*   `AI_Assignment_2_Visualization.py`: A supplementary script that uses `matplotlib` to draw a visual flowchart of the final route.
*   `README.md`: This instruction file[cite: 10].

### Execution Instructions
To execute the code and view the results, follow these steps:

1.  Open your Terminal (macOS/Linux) or Command Prompt / PowerShell (Windows).
2.  Navigate to the directory where the unzipped files are located using the `cd` command[cite: 10]:
    `cd path/to/assignment_folder`

**To run the A* Search Algorithm:**
3. Execute the main script to calculate the route[cite: 10]:
    `python AI_Assignment_2.py`

**To generate the Route Visualization:**
4. After verifying the route, execute the visualization script to generate a graphical flowchart[cite: 8]:
    `python "AI Assignment 2 Visualization.py"`

### Expected Output

**1. Main Script Output (`AI_Assignment_2.py`)**
Upon successful execution, the terminal will output the optimal step-by-step path determined by the A* Search algorithm, followed by the total estimated travel time in minutes[cite: 10]. 

```text
A* Search for the House Visit Tour

Step-by-Step Path:
  0. Sunway University
  1. Puchong
  2. Petaling Jaya
  3. Subang Jaya
  4. Shah Alam
  5. Klang

Total Estimated Travel Time: 96 minutes
