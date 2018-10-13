#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from graph_tool.all import *

f = open('C-large.in','r')
g = open('C-large.ou','w')


def buildGraph(N, H, D):
    myGraph1 = Graph()
    vlist1 = myGraph1.add_vertex(N)
    weight = myGraph1.new_edge_property("double")
    for i in range(N):
        for j in range(N):
            if D[i,j] != -1:
                e = myGraph1.add_edge(i,j)
                weight[e] = D[i,j]
    myGraph2 = Graph()
    vlist2 = myGraph2.add_vertex(N)
    time = myGraph2.new_edge_property("float")
    for i in range(N):
        for j in range(N):
            if i!=j:
                dist = graph_tool.topology.shortest_distance(myGraph1, i, j, weight)
                if dist <= H[i][0]:
                    e = myGraph2.add_edge(i,j)
                    time[e] = dist/H[i][1]
    return myGraph2, time
    





n = int(f.readline()[:-1])
for k in range(n):
    print(k)
    line = f.readline()[:-1].split()
    N = int(line[0])
    Q = int(line[1])
    H = []#horses
    for i in range(N):
        line_i = f.readline()[:-1].split()
        Ei = int(line_i[0])
        Si = int(line_i[1])
        H += [(Ei, Si)]
    D = np.zeros((N,N), dtype=int)
    for i in range(N):
        row_i = f.readline()[:-1].split()
        for j in range(N):
            D_ij = int(row_i[j])
            D[i,j] += D_ij
    myGraph, time = buildGraph(N, H, D)
    solution = ""
    for i in range(Q):
        line_i = f.readline()[:-1].split()
        Ui = int(line_i[0])
        Vi = int(line_i[1])
        solution += " "+ str(graph_tool.topology.shortest_distance(myGraph, Ui-1, Vi-1, time))
    g.write('Case #'+str(k+1)+':'+solution+'\n')



f.close()
g.close()
