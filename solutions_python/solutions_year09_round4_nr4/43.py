#!/usr/bin/env python

from math import *

INF = 1000000000

def solve(pair, ind):
  ans = max(ind[2], (sqrt((pair[0][0] - pair[1][0])**2 + (pair[0][1] - pair[1][1])**2) + pair[0][2] + pair[1][2]) / 2.0)
  return ans

for case in xrange(1, int(raw_input())+1):
  N = int(raw_input())
  plants = [map(int, raw_input().split()) for _ in xrange(N)]
  ans = INF
  if N == 1:
    ans = plants[0][2]
  elif N == 2:
    ans = max(plants[0][2], plants[1][2])
  else:
    for i in xrange(N):
      cplants = plants[:]
      del cplants[i]
      ans = min(ans, solve(cplants, plants[i]))
  print "Case #%d: %.8f" % (case, ans)
