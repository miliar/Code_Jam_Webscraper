#!/usr/bin/python

import sys

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()

  S = toks[0]
  R = []
  for c in S:
    if c == '+':
      R.append(1)
    else:
      R.append(0)
  K = int(toks[1])

  flips = 0
  for i in xrange(len(R) - K + 1):
    if R[i] == 0: # flip!
      for j in xrange(i, i + K):
        R[j] = 1 - R[j]
      flips += 1

  check = True
  for i in xrange(len(R) - K, len(R)):
    if R[i] == 0:
      check = False
      break

  if check:
    print "Case #%d: %d" % (test+1, flips)
  else:
    print "Case #%d: IMPOSSIBLE" % (test+1)

