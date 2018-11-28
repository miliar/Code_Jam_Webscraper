#!/usr/bin/env python3

from sys import stdin as I

def solve(T):
  D, N = map(int, I.readline().split())
  G = 0.0

  for i in range(N):
    P, S = map(int, I.readline().split())
    g = float(D - P) / float(S)
    G = max(G, g)

  S = float(D) / G
  print("Case #%i: %f" % (T, S))

T = int(I.readline())
for i in range(T):
  solve(i + 1)
