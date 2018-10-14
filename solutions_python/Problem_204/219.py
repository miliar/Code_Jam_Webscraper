# Python program for implementation of Ford Fulkerson algorithm
  
from collections import defaultdict
import math
  
#This class represents a directed graph using adjacency matrix representation
class Graph:
  
    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        #self.COL = len(gr[0])
         
  
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)
         
        # Create a queue for BFS
        queue=[]
         
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
         
        # Standard BFS Loop
        while queue:
 
            #Dequeue a vertex from queue and print it
            u = queue.pop(0)
         
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False
             
     
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
  
# Create a graph given in the above diagram
 
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 5
  

def MaximumKits(R, Q):
  # Get the range of each entry
  N = len(Q)
  P = len(Q[0])
  ranges = [[[0, 0] for _ in range(P)] for _ in range(N)]
  for i in range(N):
    for j in range(P):
      ranges[i][j] = [math.ceil(Q[i][j] / (1.1 * R[i])), math.floor(Q[i][j] / (0.9 * R[i]))]
  # Connect each consecutive rows
  # ranges[i][j] is the (i * P + j)-th entry
  # source is NP, sink is NP + 1
  n_nodes = N * P + 2
  source = N * P
  sink = N * P + 1
  graph = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]
  for p in range(P): # connect sink to first layer
    l, u = ranges[0][p]
    if 1 <= l <= u:
      graph[source][p] = 1
  for p in range(P): # connect last layer to sink
    l, u = ranges[N - 1][p]
    if 1 <= l <= u:
      graph[(N - 1) * P + p][sink] = 1
  for n in range(N - 1): # connect layer n to layer n + 1
    for p1 in range(P):
      for p2 in range(P): # check if ranges[n][p1] and ranges[n + 1][p2] intersects
        l1, u1 = ranges[n][p1]
        l2, u2 = ranges[n + 1][p2]
        if l1 <= u1 and l2 <= u2 and l1 <= u2 and l2 <= u1:
          graph[n * P + p1][(n + 1) * P + p2] = 1
  # Solve the max flow problem
  g = Graph(graph)
  max_card_flow = g.FordFulkerson(source, sink)
  return max_card_flow

if __name__ == '__main__':
  T = int(input())
  for i in range(1, T + 1):
    N, P = list(map(int, input().split(' ')))
    R = list(map(int, input().split(' ')))
    Q = [[0 for _ in range(P)] for _ in range(N)]
    for j in range(N):
      Q[j] = list(map(int, input().split(' ')))
    output = MaximumKits(R, Q)
    print('Case #{}: {}'.format(i, output))
