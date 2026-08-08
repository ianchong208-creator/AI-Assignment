import heapq

# 1. Graph Data Structure
# Representing the locations and travel times (in minutes) as an adjacency list.
# Based on the data collected from Google Maps in Assignment 1.
graph = {
    'Sunway University': {'Subang Jaya': 13, 'Puchong': 18, 'Shah Alam': 21, 'Petaling Jaya': 34, 'Klang': 27},
    'Subang Jaya': {'Sunway University': 13, 'Puchong': 16, 'Shah Alam': 19, 'Petaling Jaya': 20, 'Klang': 34},
    'Puchong': {'Sunway University': 18, 'Subang Jaya': 16, 'Shah Alam': 26, 'Petaling Jaya': 24, 'Klang': 34},
    'Shah Alam': {'Sunway University': 21, 'Subang Jaya': 19, 'Puchong': 26, 'Petaling Jaya': 39, 'Klang': 15},
    'Petaling Jaya': {'Sunway University': 34, 'Subang Jaya': 20, 'Puchong': 24, 'Shah Alam': 39, 'Klang': 40},
    'Klang': {'Sunway University': 27, 'Subang Jaya': 34, 'Puchong': 34, 'Shah Alam': 15, 'Petaling Jaya': 40}
}

# The target set of residential locations that must be visited
REQUIRED_LOCATIONS = {'Subang Jaya', 'Puchong', 'Shah Alam', 'Petaling Jaya', 'Klang'}

# 2. Heuristic Function h(n)
def get_heuristic(current_location, visited_locations):
    """
    Calculates the estimated remaining travel time.
    Finds the minimum edge cost from the current location to any unvisited required residential area.
    """
    unvisited = REQUIRED_LOCATIONS - set(visited_locations)

    if not unvisited:
        return 0  # Goal reached; no more travel needed

    min_time = float('inf')
    for target in unvisited:
        if target in graph[current_location]:
            min_time = min(min_time, graph[current_location][target])

    # Return the minimum time, or 0 if somehow disconnected (safety catch)
    return min_time if min_time != float('inf') else 0

# 3. Main Search Algorithm
def a_star_tour(start_location):
    """
    Executes the A* Search algorithm to find the optimal house visit tour.
    """
    # Priority Queue (Frontier): Stores tuples of (f_cost, g_cost, current_location, visited_locations, path)
    pq = []

    # Initial state setup (Using a tuple for visited states so it can be hashed in our explored set)
    initial_visited = tuple()
    initial_h = get_heuristic(start_location, initial_visited)

    # Push the initial state into the frontier
    # heapq automatically sorts by the first element of the tuple, which is our f(n) cost
    heapq.heappush(pq, (initial_h, 0, start_location, initial_visited, [start_location]))

    # Visited States (Closed List): Stores tuples of (current_location, visited_locations_tuple)
    explored = set()

    # 4. Search Loop
    while pq:
        # Pop the state with the lowest f(n) from the Priority Queue
        f_cost, g_cost, current_location, visited, path = heapq.heappop(pq)

        # 5. Goal Test
        if set(visited) == REQUIRED_LOCATIONS:
            return path, g_cost  # Return the optimal route array and the total travel time

        # Check if we have already explored this exact state
        state_key = (current_location, visited)
        if state_key in explored:
            continue

        # Mark this state as explored
        explored.add(state_key)

        # Expand neighboring locations
        for neighbor, travel_time in graph[current_location].items():

            # Update the visited locations tracker if the neighbor is one of the required houses
            new_visited = set(visited)
            if neighbor in REQUIRED_LOCATIONS:
                new_visited.add(neighbor)
            new_visited_tuple = tuple(sorted(new_visited))

            # If this specific transition has already been fully explored, skip it
            if (neighbor, new_visited_tuple) in explored:
                continue

            # Calculate the exact accumulated cost g(n) and the new heuristic h(n)
            new_g_cost = g_cost + travel_time
            new_h_cost = get_heuristic(neighbor, new_visited_tuple)

            # Calculate the evaluation function f(n) = g(n) + h(n)
            new_f_cost = new_g_cost + new_h_cost

            # Record the path taken so far
            new_path = path + [neighbor]

            # Push the generated successor state back into the Priority Queue
            heapq.heappush(pq, (new_f_cost, new_g_cost, neighbor, new_visited_tuple, new_path))

    return None, float('inf') # Fallback if no solution exists

# Execution Block
if __name__ == "__main__":
    print("A* Search for the House Visit Tour")

    optimal_route, total_time = a_star_tour('Sunway University')

    if optimal_route:
        print("\nStep-by-Step Path:")
        for i, location in enumerate(optimal_route):
            print(f"  {i}. {location}")

        print(f"\nTotal Estimated Travel Time: {total_time} minutes")
    else:
        print("\n[ERROR] No valid route could be found to visit all locations.")