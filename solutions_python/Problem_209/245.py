#!/usr/bin/python3
# A: Ample Syrup

import heapq
import math

T = int(input())
for case in range(T):
  N, K = input().split(' ')
  N, K = int(N), int(K)

  pancakes = {}
  for _ in range(N):
    R, H = input().split(' ')
    R, H = int(R), int(H)
    if R not in pancakes:
      pancakes[R] = ()
    pancakes[R] += (H,)

  result = 0
  cakes = []
  for r in sorted(pancakes.keys()):
    flag = False
    maxh = 0
    for h in pancakes[r]:
      h *= math.pi * r * 2
      if len(cakes) == K:
        if h != heapq.heappushpop(cakes, h):
          flag = True
        else:
          maxh = max(maxh, h)
      else:
        heapq.heappush(cakes, h)
        flag = True
    if not flag:
      prevh = heapq.heapreplace(cakes, maxh)
    new_result = max(result, math.pi * r * r + sum(cakes))
    if new_result > result:
      result = new_result
    elif flag:
      heapq.heapreplace(cakes, prevh)

  print('Case #%d: %s' % (case + 1, result))
