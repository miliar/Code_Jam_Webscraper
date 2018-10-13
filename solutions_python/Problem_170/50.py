#!/usr/bin/env python3

# Edmonds Karp algorithm for solving the max-flow problem
# https://github.com/bigbighd604/Python/blob/master/graph/Edmonds-Karp.py

import decimal

def EdmondsKarp(capacity, neighbors, start, end):
  flow = 0
  length = len(capacity)
  flows = [[0 for i in range(length)] for j in range(length)]
  while True:
    max, parent = BreadthFirstSearch(capacity, neighbors, flows, start, end)
    if max == 0:
      break
    flow = flow + max
    v = end
    while v != start:
      u = parent[v]
      flows[u][v] = flows[u][v] + max
      flows[v][u] = flows[v][u] - max
      v = u
  return (flow, flows)

def BreadthFirstSearch(capacity, neighbors, flows, start, end):
  length = len(capacity)
  parents = [-1 for i in range(length)] # parent table
  parents[start] = -2 # make sure source is not rediscovered
  M = [0 for i in range(length)] # Capacity of path to vertex i
  M[start] = decimal.Decimal('Infinity') # this is necessary!

  queue = []
  queue.append(start)
  while queue:
    u = queue.pop(0)
    for v in neighbors[u]:
      # if there is available capacity and v is is not seen before in search
      if capacity[u][v] - flows[u][v] > 0 and parents[v] == -1:
        parents[v] = u
        # it will work because at the beginning M[u] is Infinity
        M[v] = min(M[u], capacity[u][v] - flows[u][v]) # try to get smallest
        if v != end:
          queue.append(v)
        else:
          return M[end], parents
  return 0, parents

# Solve the problem by reduction to max-flow

from collections import defaultdict

def solve(N, phrase):
    W = set(w for p in phrase for w in p)
    I = {}
    for i, w in enumerate(W):
        I[w] = N+i
    C = {}
    Ne = {}
    for i in range(N):
        C[i] = defaultdict(int)
        Ne[i] = set()
    for w in W:
        C[I[w]] = defaultdict(int)
        Ne[I[w]] = set()
    for w in phrase[0]:
        C[0][I[w]] = C[I[w]][0] = 1
        Ne[0].add(I[w])
        Ne[I[w]].add(0)
    for w in phrase[1]:
        C[1][I[w]] = C[I[w]][1] = 1
        Ne[1].add(I[w])
        Ne[I[w]].add(1)
    for i in range(2, N):
        for w in phrase[i]:
            C[i][I[w]] = C[I[w]][i] = 1
            Ne[i].add(I[w])
            Ne[I[w]].add(i)
    return EdmondsKarp(C, Ne, 0, 1)[0]

import sys
sys.setrecursionlimit(10000)

tests = int(input())
for test in range(tests):
    N = int(input())
    phrase = []
    for i in range(N):
        phrase.append(input().split())
    result = solve(N, phrase)
    print("Case #{}: {}".format(1+test, result))
