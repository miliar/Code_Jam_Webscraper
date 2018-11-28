#!/usr/bin/python

import sys

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()

  N = [ int(i) for i in toks[0] ]
  L = len(N)

  for i in xrange(L - 1):
    ir = L - i - 1
    a = N[ir - 1]
    b = N[ir]
    if a > b: # not tidy
      N[ir - 1] = a - 1
      for j in xrange(ir, L):
        N[j] = 9

  sol = ''
  nz = False
  for i in N:
    if i > 0:
      nz = True
    if nz:
      sol += str(i)

  print "Case #%d: %s" % (test+1, sol)

