t = int(raw_input())  # read a line with a single integer

import numpy as np


# Python program for implementation of Ford Fulkerson algorithm
# A note from paruby: the implementation of ford fulkerson
# is taken from http://www.geeksforgeeks.org/maximum-bipartite-matching/

from collections import defaultdict


# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    #'''Returns true if there is a path from source 's' to sink 't' in
    #residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


for i in xrange(1, t + 1):
    string_N, string_M = [s for s in raw_input().split(" ")]
    N = int(string_N)
    M = int(string_M)

    grams = raw_input().split(" ")
    array_of_portions = []

    for n in range(0,N):
        list_of_sizes = raw_input().split(" ")
        list_of_portions = []
        for k in range(0,len(list_of_sizes)):
            size = float(list_of_sizes[k])
            upperN = np.floor(size/(0.9*float(grams[n])))
            lowerN = np.ceil(size/(1.1*float(grams[n])))
            #print lowerN
            #print upperN
            list_of_portions.append(range(int(lowerN), int(upperN)+1))

        array_of_portions.append(list_of_portions)

    graph = [[0 for l in range(0, N*M + 2)] for j in range(0, N*M + 2)]
    #all first row nodes have incoming arrow from source
    #all last row nodes that have some allowable portion have outgoing arrow to sink
    for m in range(0,M):
        graph[0][m+1] = 1
        if array_of_portions[-1][m] !=[]:
            graph[(N-1)*M+m+1][-1] = 1

    #for all other rows, there should be outgoing arrows to nodes that match on allowed portions
    for n in range(0,N-1):
        for m in range(0,M):
            for m2 in range(0,M):
                if bool(set(array_of_portions[n][m]) & set(array_of_portions[n+1][m2])):
                    graph[n*M + m+1][(n+1)*M + m2+1] = 1
    g = Graph(graph)
    max_flow = g.FordFulkerson(0,N*M+1)

    print "Case #{}: {}".format(i, max_flow)
  # check out .format's