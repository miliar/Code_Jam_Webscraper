from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'C-large.in'

endurance = 0
speed = 1

inf = 10**100

def floyd_warshall(n, edges):
    dst = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if edges[i][j] == -1:
                dst[i][j] = inf
            else:
                dst[i][j] = edges[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])
    return dst

def _solve(n, cities, edges, queries):
    dst = floyd_warshall(n, edges)
    hedges = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dst[i][j] <= cities[i][endurance]:
                hedges[i][j] = dst[i][j] / cities[i][speed]
            else:
                hedges[i][j] = -1
    hdst = floyd_warshall(n, hedges)
    res = []
    #print(hdst, queries)
    for f, t in queries:
        res.append(hdst[f - 1][t - 1])
    return ' '.join(map(str, res))

def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return res

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    (n, q) = tuple(map(int, inp_file.readline().split()))
    cities = []
    edges = []
    queries = []
    for i in range(n):
        cities.append(tuple(map(int, inp_file.readline().split())))
    for i in range(n):
        edges.append(tuple(map(int, inp_file.readline().split())))
    for i in range(q):
        queries.append(tuple(map(int, inp_file.readline().split())))
    res = solve(n, cities, edges, queries)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()









