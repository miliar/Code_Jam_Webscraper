#!/usr/bin/env python3

import math
from sys import stdin as I

def solve(T):
  N, Q = map(int, I.readline().split())

  H = []
  for i in range(N):
    H.append(list(map(int, I.readline().split())))

  D = []
  for i in range(N):
    D.append(list(map(int, I.readline().split())))

  for i in range(Q):
    U, V = map(int, I.readline().split())

    Hs = [[] for i in range(N)]
    Bs = [0.0] * N

    for horse in range(N):
      remaining = H[horse][0]
      dest = horse + 1
      while dest < N:
        dist = D[dest-1][dest]
        if dist <= remaining:
          Hs[dest].append(horse)
          remaining -= dist
          dest += 1
        else:
          break
    for dest in range(1, N):
      options = []
      for horse in Hs[dest]:
        dist = 0.0
        for x in range(horse, dest):
          dist += D[x][x+1]
        options.append(Bs[horse] + float(dist) / float(H[horse][1]))
      Bs[dest] = min(options)

  print("Case #%i: %f" % (T, Bs[-1]))

T = int(I.readline())
for i in range(T):
  solve(i + 1)
