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
def dfs(graph, start):
    visited = set()  # To keep track of visited nodes
    stack = [start]  # Use stack for DFS

    while stack:
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)

            # Add unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Run DFS starting from 'S'
print("DFS traversal starting from node 'S':")
dfs(graph, 'S')
print("\n")


def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Use queue for BFS

    while queue:
        node = queue.popleft()  # Dequeue a node from the queue
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)

            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Run BFS starting from 'S'
print("BFS traversal starting from node 'S':")
bfs(graph, 'S')

#DFS (Depth-First Search):
#['S', 'd', 'b', 'a', 'c', 'e', 'h', 'p', 'q', 'r', 'f', 'G']

#BFS (Breadth-First Search):
#['S', 'd', 'e', 'p', 'b', 'c', 'h', 'r', 'q', 'a', 'f', 'G']


# DFS implementation
#def dfs(graph, start, visited=None):
 #   if visited is None:
  #      visited = set()
  #  visited.add(start)
   # print(start, end=" ")
    #for neighbor in graph.get(start, []):
     #   if neighbor not in visited:
      #      dfs(graph, neighbor, visited)

# BFS implementation
#def bfs(graph, start):
 #   visited = set([start])
   # queue = deque([start])
  #  while queue:
       # node = queue.popleft()
       # print(node, end=" ")
      #  for neighbor in graph.get(node, []):
         #   if neighbor not in visited:
        #        visited.add(neighbor)
       #         queue.append(neighbor)
