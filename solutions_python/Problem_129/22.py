#!/usr/bin/env python

from sys import argv

f = open(argv[1])
T = int(f.readline().strip())
for tc in xrange(1, T+1):
  N, M = map(int, f.readline().strip().split(' '))
  woswap = 0
  dd = {}
  for i in xrange(M):
    o, e, p = map(int, f.readline().strip().split(' '))
    woswap += p * (e-o)**2
    dd[o] = dd.get(o, 0) + p
    dd[e] = dd.get(e, 0) - p
  dl = sorted(dd.keys())
  withswap = 0
  bd = {}
  bl = []
  for s in dl:
    if dd[s] > 0:
      bd[s] = dd[s]
      bl.append(s)
    p = -dd[s]
    while p > 0:
      o = bl[-1]
      while bd[o] < p:
        withswap += bd[o] * (s-o)**2
        p -= bd[o]
        bd[o] = 0
        bl.pop()
        if p > 0:
          o = bl[-1]
      withswap += p * (s-o)**2
      bd[o] -= p
      p = 0
  ans = (withswap-woswap)//2
  ans %= 1000002013
  print "Case #%d: %d" % (tc, ans)

