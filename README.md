# Depth First Search and Breadth First Search 
First algorithms are depth first search and breadth first search.
# Breadth First Search
- What nodes does BFS expand?
  - Processes all nodes above shallowest solution
  - Let depth of shallowest solution be s
  - Search takes time O(b^s)
- How much space does the fringe take?
  - Has roughly the last tier, so O(b^s)
  - Is it complete?
  - s must be finite if a solution exists, so yes!
- Is it optimal?
  - Only if costs are all 1 
# Depth First Search
- What nodes does DFS expand?
  - Some left prefix of the tree.
  - Could process the whole tree!
  - If m is finite, takes time O(b^m)
- How much space does the fringe take?
  - Only has siblings on path to root, so O(bm)
- Is it complete?
  - m could be infinite, so only if we prevent 
cycles 
 - Is it optimal?
   - No, it finds the “leftmost” solution, 
regardless of depth or cost.
