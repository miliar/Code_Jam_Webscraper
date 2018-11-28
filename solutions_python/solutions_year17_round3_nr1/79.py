#!/usr/bin/env python

import sys
import numpy as np

T = int(raw_input())

for t in xrange(T):
  # solve the input
  N, K = raw_input().strip().split()
  N = int(N)
  K = int(K)

  RH = np.zeros(N)
  tuples = []
  for n in xrange(N):
    r, h = raw_input().strip().split()
    RH[n] = 2 * float(r) * float(h)
    tuples.append((float(r), RH[n]))

  tuples.sort(reverse=True)

  maxSyrup = -1
  for n in xrange(N-K+1): # potential starts
    syrup = tuples[n][0]**2 + tuples[n][1]

    remaining = sorted(tuples[n+1:], key=lambda x: x[1], reverse=True)
    syrup += sum([x[1] for x in remaining[0:K-1]])
    if syrup > maxSyrup:
      maxSyrup = syrup

  print "Case #{0}: {1}".format(t+1, np.pi * maxSyrup) 
