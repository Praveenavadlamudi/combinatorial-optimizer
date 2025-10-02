import math

def tsp_greedy(tsp_data):
    if not tsp_data:
        return []

    visited = [tsp_data[0]]
    remaining = tsp_data[1:]
    current = tsp_data[0]

    while remaining:
        next_city = min(remaining, key=lambda city: math.dist((city[1], city[2]), (current[1], current[2])))
        visited.append(next_city)
        remaining.remove(next_city)
        current = next_city

    visited.append(tsp_data[0])
    return visited


def knapsack_greedy(knapsack_data, capacity=50):
    sorted_items = sorted(knapsack_data, key=lambda x: x[2]/x[1] if x[1] > 0 else 0, reverse=True)
    total_weight = 0
    total_value = 0
    selected = []

    for item in sorted_items:
        if total_weight + item[1] <= capacity:
            selected.append(item)
            total_weight += item[1]
            total_value += item[2]

    return selected, total_value, total_weight
