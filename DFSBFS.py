from collections import deque

# Define the graph as an adjacency list
graph = {
    'S': ['d', 'e', 'p'],
    'd': ['b', 'c', 'e'],
    'e': ['h', 'r'],
    'h': ['p', 'q'],
    'p': ['q'],
    'r': ['f'],
    'f': ['c', 'G'],
    'c': ['a'],
    'b': ['a']
}

# DFS implementation
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS implementation
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Run DFS starting from 'S'
print("DFS traversal starting from node 'S':")
dfs(graph, 'S')
print("\n")

# Run BFS starting from 'S'
print("BFS traversal starting from node 'S':")
bfs(graph, 'S')
