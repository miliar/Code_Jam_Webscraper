#!/usr/bin/env python

import sys
import numpy as np

inputs = [line.strip() for line in sys.stdin]

T = int(inputs[0])

for t in xrange(T):
  # solve the input
  N = inputs[t+1]
  arr = [int(N[i]) for i in xrange(len(N))]
  nines = len(arr)
  i = 0
  while i < nines - 1:
    if arr[i] > arr[i+1]:
      # now need to fix this
      arr[i] = arr[i] - 1
      nines = i+1
      i = 0 # start again
      continue
    i += 1
  
  for j in xrange(nines, len(arr)):
    arr[j] = 9

  num = "".join([str(i) for i in arr]).lstrip('0')
  print "Case #{0}: {1}".format(t+1, num)

