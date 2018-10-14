#!/usr/bin/env python

import sys
import numpy as np

inputs = [line.strip() for line in sys.stdin]

T = int(inputs[0])

for t in xrange(T):
  # solve the input
  init, K = inputs[t+1].split()
  K = int(K)
  N = len(init)
  arr = np.array([init[i] == '+' for i in xrange(N)])#np.zeros(len(init))
  count = 0
  
  # fix them
  for i in xrange(N - K + 1):
    if not arr[i]: # it's a minus
      count += 1
      for k in xrange(K):
        arr[i+k] = not arr[i+k]

  # check the rest
  possible = True
  for i in xrange(N - K + 1, N):
    if not arr[i]:
      print "Case #{0}: IMPOSSIBLE".format(t+1)
      possible = False
      break
      
  if possible:
    print "Case #{0}: {1}".format(t+1, count)

