#!/usr/bin/python
# -*- coding: utf-8 -*-
# Google Code Jam template

from __future__ import print_function, division, absolute_import, unicode_literals
import collections
import time
import sys
import os
import random
import numpy as np
import scipy as sp
import networkx as nx
import operator
import copy
import networkx as nx

sys.setrecursionlimit(sys.getrecursionlimit()*3)


def solve(N,Ei,Si,Dij,U,V):
    graph = nx.DiGraph()
    for i in range(N):
        for j in range(N):
            if i==j: continue
            if Dij[i][j]>0:
                graph.add_edge(i,j,weight=Dij[i][j])
    graph2 = nx.DiGraph()
    for i in range(N):
        for t,d in nx.single_source_dijkstra_path_length(graph,i,cutoff=Ei[i]).items():
            if d>0:
                w = weight=d/Si[i]
                if graph2.has_edge(i,t):
                    print("hey",w,graph2[i][t]['weight'])
                    w = min(w,graph2[i][t]['weight'])
                    graph2[i][t]['weight']=w
                else:
                    graph2.add_edge(i,t,weight=d/Si[i])

    solution = ""
    for i in range(len(U)):
        solution += "%.8f " % (nx.shortest_path_length(graph2,U[i]-1,V[i]-1,weight='weight'),)
    return solution

T = int(sys.stdin.readline())
for t in range(1,T+1):
    N, Q = map(int,sys.stdin.readline().split())
    Ei,Si=[],[]
    Dij = []
    for i in range(N):
        ei,si= map(int,sys.stdin.readline().split())
        Ei.append(ei)
        Si.append(si)
    for i in range(N):
        Dij.append(map(int,sys.stdin.readline().split()))
    U,V=[],[]
    for i in range(Q):
        u,v = map(int,sys.stdin.readline().split())
        U.append(u)
        V.append(v)
    solution = solve(N,Ei,Si,Dij,U,V)
    print("Case #%i: %s" % (t,solution))
