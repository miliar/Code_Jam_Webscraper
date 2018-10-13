#!/usr/bin/python3
# C: Core Training

import functools
import heapq
import operator

T = int(input())
for case in range(T):
  N, K = input().split(' ')
  N, K = int(N), int(K)
  U = float(input())

  P = [float(p) for p in input().split(' ')]
  heapq.heapify(P)

  if K == N:
    n = 2
    while U > 1e-12:
      smallest = heapq.nsmallest(n, P)
      diff = smallest[-1] - smallest[0]
      if diff == 0 and n < K:
        n += 1
      elif diff == 0:
        P = [smallest[0] + U / K] * N
        U = 0
      elif diff * (n - 1) >= U:
        for _ in range(n - 1):
          heapq.heappushpop(P, smallest[0] + U / (n - 1))
        U = 0
      else:
        for _ in range(n - 1):
          heapq.heappushpop(P, smallest[0] + diff)
        U -= diff * (n - 1)
        n += 1
      if n > K:
        n = K
    result = functools.reduce(operator.mul, P, 1)
  else:
    result = 0

  print('Case #%d: %s' % (case + 1, result))
