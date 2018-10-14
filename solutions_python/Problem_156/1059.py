#!/usr/bin/python

import sys, math

def min_time(P):
  P.sort(reverse=True)
  p0 = P[0]
  mt = p0;

  if p0 > 2:
    # print >> sys.stderr, "@1",P
    # np = p0 / 2
    for np in range(2, 1+p0/2):
      P[0] = p0 - np
      Q = list(P)
      Q.append(p0 - P[0])
      # print >> sys.stderr, "@2",Q
      t = 1 + min_time(Q)
      if t < mt:
        mt = t

  return mt

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  D = int(sys.stdin.readline())
  toks = sys.stdin.readline().strip().split()
  P = [int(t) for t in toks]
  if D != len(P):
    print >> sys.stderr, "Malformed input!"
    raise

  # print >> sys.stderr, P

  y = min_time(P)

  print "Case #%d: %d" % (test+1, y)

