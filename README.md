Combinatorial Optimizer

A unified Python framework to solve combinatorial optimization problems like TSP (Traveling Salesman Problem), Knapsack Problem, and Graph Matching using multiple strategies. This project demonstrates classical algorithms and heuristics, compares their performance, and provides an easy-to-use interface for experimentation.

Features

TSP (Traveling Salesman Problem)

Greedy heuristics

Finds an approximate shortest tour visiting all cities

Knapsack Problem

Greedy heuristic for selecting items maximizing value under weight constraints

Extendable framework

Easily add Backtracking, Branch & Bound, Dynamic Programming, and other heuristics

Performance tracking

Measure execution time of each algorithm

Clean and modular code

Organized in separate modules for strategies, utilities, and experiments

Folder Structure
combinatorial-optimizer/
│
├─ main.py                  # Main script to run experiments
├─ README.md                # Project description
├─ requirements.txt         # Python dependencies
├─ strategies/              # Algorithm implementations
│   ├─ __init__.py
│   └─ greedy.py
├─ utils/                   # Utility functions (e.g., performance measurement)
│   ├─ __init__.py
│   └─ performance.py
└─ data/                    # Sample datasets for TSP, Knapsack, etc.

Installation

Clone the repository:

git clone https://github.com/Praveenavadlamudi/combinatorial-optimizer.git
cd combinatorial-optimizer


Create a virtual environment:

python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


Install dependencies:

pip install -r requirements.txt

Usage

Run the main experiment script:

python main.py


Modify main.py to test different datasets and algorithms.

Contributing

Contributions are welcome!

Add new strategies (e.g., Backtracking, Branch & Bound)

Improve existing heuristics

Add more datasets for testing

License

This project is open-source and available under the MIT License.
