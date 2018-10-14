from __future__ import division

from sys import stdin, stdout
from basics import *
import networkx as nx

def solve_small(N, Q, towns, network, paths):
    G = nx.Graph()
    for i in range(N-1):
        max_dist, speed = towns[i]

        so_far = 0
        for j in range(i+1, N):
            so_far += network[j-1][j]

            if so_far <= max_dist:
                G.add_edge(i, j, weight = so_far / speed)
            else:
                break

    return nx.dijkstra_path_length(G, source=0, target=N-1)



T = int(stdin.readline())

for t in range(T):
    N, Q = read_vals()
    towns = read_lines(N)
    network = read_lines(N)
    paths = read_lines(Q)

    result = solve_small(N, Q, towns, network, paths)

    stdout.write("Case #{}: {}\n".format(t+1, result))