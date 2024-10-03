class Node:
    def __init__(self, name):
        self.name = name
        self.g = float('inf')  # Cost from the start node
        self.f = float('inf')  # Total cost
        self.parent = None

graph = {
    'S': [('A', 3), ('B', 2), ('C', 5)],
    'A': [('G', 2), ('C', 3)],
    'B': [('A', 4), ('D', 6)],
    'C': [('B', 4), ('H', 3)],
    'G': [('D', 4), ('E', 5)],
    'E': [('F', 5)],
    'H': [('D', 4)],
    'D': [('E', 2), ('F', 3)],
    'F': []
}

# Graph of Heuristic values
heuristics = {
    'S': 10, 'A': 8, 'B': 7, 'C': 6,
    'D': 4, 'E': 3, 'F': 0, 'G': 6, 'H': 5
}
# Create a node for each element in the graph and add to nodes dictionary
nodes = {}
for key in graph:
    nodes[key] = Node(key)

def AStar(start, goal):
    # Initialize the source
    source = nodes[start]
    source.g = 0
    # f(n) = g(n) + h(n)
    # heuristics[start] Gets the heuristic value of the starting node
    source.f = source.g + heuristics[start]

    # Initialize the queue and visited set
    queue = [source]
    visited = set()

    while queue:
        # Gets the f value per node
        def get_f(node):
            return node.f
        # Sort queue by f value and pop the lowest
        queue.sort(key=get_f)
        current_node = queue.pop(0)

        # Check if the destination is reached
        if current_node.name == goal:
            return construct_path(current_node)

        # Mark the current node as visited
        visited.add(current_node.name)

        # Explore neighbors
        # Based off the current node in the graph, iterates through the name and cost of each neighbor
        neighbors = graph[current_node.name]
        for name, cost in neighbors:
            neighbor = nodes[name]
            if neighbor.name in visited:
                continue  # Skip nodes already visited

            # Calculate the new g value
            temp_g = current_node.g + cost

            if temp_g < neighbor.g:
                # This path is better; update neighbor
                neighbor.g = temp_g
                neighbor.f = neighbor.g + heuristics[neighbor.name]
                neighbor.parent = current_node

                if neighbor not in queue:
                    queue.append(neighbor)  # Add to queue if not already there

    return False


def construct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Return the path in reverse order


path = AStar('S', 'F')
print("Path:", path)
