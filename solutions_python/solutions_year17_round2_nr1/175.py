#!/usr/bin/env python

import sys
import numpy as np

inputs = [line.strip() for line in sys.stdin]

T = int(inputs[0])

pos = 0
for t in xrange(T):
  # solve the input
  pos = pos+1 

  D, N = inputs[pos].split()
  D = float(D)
  N = int(N)

  Tmax = -1

  for n in xrange(N):
    pos = pos+1
    K, S = inputs[pos].split()
    K = int(K)
    S = float(S)
    T =  (D - K) / S
    Tmax = np.maximum(T, Tmax)

  v = D / Tmax
  print "Case #{0}: {1}".format(t+1, v)

  
