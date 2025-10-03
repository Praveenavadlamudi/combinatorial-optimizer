
from flask import Flask, render_template, request
from problems.tsp import load_tsp_data
from problems.knapsack import load_knapsack_data
from problems.graph_matching import load_graph_data
from strategies.greedy import tsp_greedy, knapsack_greedy
from strategies.dynamic_programming import tsp_dp, knapsack_dp
from strategies.backtracking import knapsack_backtracking
from utils.performance import measure_time
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)

@app.route("/", methods=["GET", "POST"])
def index():
    tsp_result = []
    knapsack_greedy_result = []
    knapsack_dp_result = []
    knapsack_bt_result = []
    graph_result = []

    if request.method == "POST":
        # Load CSVs safely
        tsp_data = load_tsp_data(os.path.join(BASE_DIR, "datasets/tsp_data.csv"))
        knapsack_data = load_knapsack_data(os.path.join(BASE_DIR, "datasets/knapsack_data.csv"))
        graph_data = load_graph_data(os.path.join(BASE_DIR, "datasets/graph_data.csv"))

        # Run algorithms with performance measure
        tsp_result = measure_time(tsp_greedy, tsp_data)
        knapsack_greedy_result = measure_time(knapsack_greedy, knapsack_data, 50)
        knapsack_dp_result = measure_time(knapsack_dp, knapsack_data, 50)
        knapsack_bt_result = measure_time(knapsack_backtracking, knapsack_data, 50)

        # TODO: Apply graph algorithm (right now it just returns raw data)
        graph_result = graph_data

    return render_template(
        "index.html",
        tsp_result=tsp_result,
        knapsack_greedy_result=knapsack_greedy_result,
        knapsack_dp_result=knapsack_dp_result,
        knapsack_bt_result=knapsack_bt_result,
        graph_result=graph_result
    )

if __name__ == "__main__":
    app.run(debug=True)
