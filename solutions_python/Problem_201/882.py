import os, sys
from heapq import heappush, heappop

with open("in.txt") as f:
  lines = [x.strip() for x in f.readlines()]

T = int(lines[0])
for txx in range(T):
  t = txx + 1
  nums = [int(x) for x in lines[t].split()]
  N = nums[0]
  K = nums[1]

  counts = dict()
  sets = [-N]
  counts[N] = 1

  k = 0
  while k < K:
    oldS = 0 - heappop(sets)
    newS = oldS - 1
    L = newS // 2
    R = newS - L
#    print(oldS, newS, L, R, k, counts[oldS])

    if L not in counts:
      counts[L] = 0
    if counts[L] == 0:
      heappush(sets, 0 - L)
    counts[L] += counts[oldS]
 
    if R > 0:
      if R not in counts:
        counts[R] = 0
      if counts[R] == 0:
        heappush(sets, 0 - R)
      counts[R] += counts[oldS]
    k += counts[oldS]

  print("Case #%d: %d %d" % (t, max(L, R), min(L, R)))
#  break