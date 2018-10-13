# https://code.google.com/codejam/contest/8294486/dashboard

import networkx as nx
import numpy as np

if __name__ == "__main__":
    filein = open('20171BC.in', 'r')
    fileout = open('20171BC.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        N, Q = map(int, filein.readline().split())
        ES = [list(map(int, filein.readline().split())) for i in range(N)]
        D = [list(map(int, filein.readline().split())) for i in range(N)]
        G = nx.DiGraph()
        G.add_nodes_from([i for i in range(N)])
        for i in range(N):
            for j in range(N):
                if D[i][j] != -1:
                    G.add_edge(i, j, weight=D[i][j])
        UV = [list(map(int, filein.readline().split())) for i in range(Q)]

        graph = nx.DiGraph()
        graph.add_nodes_from([i for i in range(N)])
        # build graph
        for i in range(N):
            for j in range(N):
                # find min distance
                try:
                    dist = nx.dijkstra_path_length(G, i, j)
                    if dist <= ES[i][0]:
                        graph.add_edge(i, j, weight=dist / ES[i][1])
                except nx.NetworkXNoPath:
                    pass

        for u, v in UV:
            try:
                dist = nx.dijkstra_path_length(graph, u - 1, v - 1)
            except:
                print(2)
            fileout.write(str(dist) + ' ')
        fileout.write('\n')

    filein.close()
    fileout.close()
