#!/usr/bin/env python3

from heapq import heappush, heappop

def process(N, K):
  heap = [-N]
  counts = {N: 1}
  while K:
    l = -heappop(heap)
    c = counts[l]
    del counts[l]
    l -= 1
    a, b = l-l//2, l//2
    if c >= K:
      return a, b
    if a in counts:
      counts[a] += c
    else:
      heappush(heap, -a)
      counts[a] = c
    if b in counts:
      counts[b] += c
    else:
      heappush(heap, -b)
      counts[b] = c
    K -= c

T = int(input())
for case in range(1, T+1):
  N, K = map(int, input().split())
  l, r = process(N, K)
  print("Case #{}: {} {}".format(case, l, r))

