# Team Orienteering Problem (TOP) Solver

## Project Overview

This repository hosts a comprehensive project that delves into solving the Team Orienteering Problem (TOP), a variant of the well-known Vehicle Routing Problem (VRP). TOP focuses on maximizing the total profit from visited nodes under strict constraints, making it a significant challenge in logistics and route planning.

## Key Features

### Problem Definition
- **Selective Node Visitation**: Not all nodes can be visited due to constraints, necessitating a selective approach to maximize the profit.
- **Multiple Constraints**: Includes limits on the number of vehicles, maximum route length, and mandatory start and end points at depots.

### Solution Techniques
- **Linear Programming**: We've modeled the problem using integer linear programming to ensure precise formulation and effective solving.
- **Heuristic Approaches**: Alternative heuristic methods are explored to provide faster solutions suitable for larger datasets.

### Technologies Used
- **PuLP**: A linear programming toolkit in Python used to define and solve the mathematical model.
- **Python**: For scripting and data handling, providing a robust platform for developing and testing optimization algorithms.

## Project Structure
- **data/**: Contains input data files defining node coordinates, profits, and other parameters.
- **src/**: Source code for the linear programming model and heuristic solutions.
- **results/**: Output files showing the results of the computations, including profit maximization and route details.

## Getting Started

### Prerequisites
Ensure you have Python installed along with the following packages:
pip install pulp numpy pandas matplotlib seaborn

### Running the Solver
Execute the main script to start the optimization process:
python run_solver.py

### Visualization
We provide visualization scripts to help you understand the route optimization graphically. These scripts plot the nodes, paths, and highlight profit-maximizing routes.
