#!/usr/bin/env python
from sys import stdin
import copy
import networkx as nx

tn = int(stdin.readline())
for ti in xrange(tn):
    n, m = map(int, stdin.readline().split())
    t = [[0 for j in xrange(n)] for i in xrange(n)]
    for i in xrange(m):
        x, r, c = stdin.readline().split()
        r, c = int(r)-1, int(c)-1
        if x == '+':
            t[r][c] = 1
        elif x == 'x':
            t[r][c] = 2
        elif x == 'o':
            t[r][c] = 3
    orig = copy.deepcopy(t)
    G = nx.DiGraph()
    s1 = [0 for i in xrange(n)]
    s2 = [0 for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if t[i][j]&2:
                s1[i] = 1
                s2[j] = 1
    for i in xrange(n):
        G.add_edge(2*n, i, {'capacity': 1-s1[i]})
        G.add_edge(n+i, 2*n+1, {'capacity': 1-s2[i]})
    for i in xrange(n):
        for j in xrange(n):
            G.add_edge(i, n+j, {'capacity': 1, 'weight': 0 if t[i][j]&2 else 1})
    f = nx.max_flow_min_cost(G, 2*n, 2*n+1)
    for i in xrange(n):
        for j in xrange(n):
            if f[i][n+j]:
                t[i][j] |= 2
    G = nx.DiGraph()
    s1 = [0 for i in xrange(10*n)]
    s2 = [0 for i in xrange(10*n)]
    for i in xrange(n):
        for j in xrange(n):
            if t[i][j]&1:
                s1[n+i-j] = 1
                s2[i+j] = 1
    for i in xrange(3*n):
        G.add_edge(10*n, i, {'capacity': 1-s1[i]})
        G.add_edge(5*n+i, 10*n+1, {'capacity': 1-s2[i]})
    for i in xrange(n):
        for j in xrange(n):
            G.add_edge(n+i-j, 5*n+i+j, {'capacity': 1, 'weight': 0 if t[i][j]&1 else 1})
    f = nx.max_flow_min_cost(G, 10*n, 10*n+1)
    for i in xrange(n):
        for j in xrange(n):
            if f[n+i-j][5*n+i+j]:
                t[i][j] |= 1
    sol = []
    su = 0
    for i in xrange(n):
        for j in xrange(n):
            x = t[i][j]
            su += (x&1)+((x&2)/2)
            if orig[i][j] != x:
                c = '.'
                if x == 1:
                    c = '+'
                elif x == 2:
                    c = 'x'
                elif x == 3:
                    c = 'o'
                sol.append((c, i+1, j+1))
    print 'Case #{0}:'.format(ti+1), su, len(sol)
    for ch, r, c in sol:
        print ch, r, c
