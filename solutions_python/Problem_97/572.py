#!/usr/bin/python2.7

import sys

t = int(sys.stdin.readline())


for tt in xrange(0, t):
  oo = []
  rr = [int(x) for x in sys.stdin.readline().strip().split()]
  out = 0
  for n in xrange(rr[0], rr[1]+1):
    s = str(n)
    l = len(s)
    for m in xrange(1, l):
      s2 = s[m:]+s[:m]
      if s2[0] == '0': continue
      nn = int(s2)
      if nn <= n: continue
      if nn > rr[1]: continue
      oo.append((s, s2))
  x = set(oo)
  print "Case #%d: %d" % (tt+1, len(x))
