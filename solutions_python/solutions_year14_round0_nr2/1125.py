#!/usr/bin/python
from __future__ import division
import sys

def solve():
  C, F, X = map(float, sys.stdin.readline().split())
  if X <= C:
    return X/2
  farmlimit = X/C - 2/F - 1
  n = 0
  total = 0
  while n < farmlimit:
    total += C/(2+n*F)
    n += 1
  total += X/(2+n*F)
  return total

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  answer = solve()
  print "Case #{0}: {1:.10f}".format(test_case, answer)

