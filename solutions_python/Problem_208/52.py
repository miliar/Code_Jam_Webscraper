#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from dijkstra import dijkstra

def main():
  t = int(stdin.readline().strip())
  for i in range(t):
    [N, Q] = list(map(int, stdin.readline().strip().split(' ')))
    hs = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
    m = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
    interesting = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(Q)]
    print("Case #{}: {}".format(i+1, solve(N, Q, hs, m, interesting)))


def solve(N, Q, hs, m, interesting):
  inf = float("inf")
  graph = dict()
  for i in range(N):
    graph[i] = dict()
  g = dict()
  for i in range(N):
    g[i] = dict()
    for j in range(N):
      if m[i][j] > -1:
        g[i][j] = m[i][j]
  for i, (e, s) in enumerate(hs):
    cost, parent = dijkstra(g, i)
    for j in range(N):
      if cost[j] <= e:
        graph[i][j] = cost[j] / s
  rs = []
  for u, v in interesting:
    cost, parent = dijkstra(graph, u-1)
    rs.append(cost[v-1])
  return " ".join(map(lambda x: "{:.6f}".format(x), rs))

if __name__=="__main__":
  main()
