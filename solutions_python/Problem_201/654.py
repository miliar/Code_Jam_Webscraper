#!/usr/bin/env python

import sys
import numpy as np
from collections import deque

inputs = [line.strip() for line in sys.stdin]

T = int(inputs[0])

def addToQ(q, counts, k, times):
  if k <= 0:
    return

  if k in counts:
    counts[k] += times
  else:
    counts[k] = times
    q.append(k)

for t in xrange(T):
  N, K = inputs[t+1].split()
  N = int(N)
  K = int(K)

  if N == K:
    print "Case #{0}: 0 0".format(t+1)
    continue

  q = deque([N])
  counts = {N: 1}

  k = K
  while k > 0:
    if len(q) == 0:
      print 0
      break

    n = q.popleft()
    
    times = counts[n]
    del counts[n]
    k -= times
    
    # add new elements
    if n % 2 == 1:
      a = (n-1)/2
      b = (n-1)/2
    else:
      a = n/2
      b = n/2 - 1
    addToQ(q, counts, a, times)
    addToQ(q, counts, b, times)
      
  print "Case #{0}: {1} {2}".format(t+1, max(a,b), min(a,b))

