#!/usr/bin/python
import sys
import itertools
import random


def optimal(dumb, smart):
  pts = 0
  dl = sorted(dumb)
  sl = sorted(smart)
  si = 0
  for di, db in enumerate(dl):
    while si < len(sl) and sl[si] < db:
      si += 1
    if si >= len(sl):
      return pts
    pts += 1
    si += 1
  return pts

def solve():
  N = int(sys.stdin.readline())
  nao =map(float, sys.stdin.readline().split())
  ken = map(float, sys.stdin.readline().split())
  return optimal(ken, nao), N-optimal(nao,ken) 

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  a, b = solve()
  print "Case #{0}: {1} {2}".format(test_case, a, b)
