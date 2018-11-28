#!/usr/bin/python

import sys


def bathrooms(N, K):
  k = 0

  # count the number of intervals with the same number of free stalls
  spaces = {N: 1}
  consumed = 0
  while k < K:
    # consume the entire level?
    avail = sum(spaces.values())

    if K-k > avail:
      k += avail

      # split the intervals in two
      spaces2 = {}
      for (n,count) in spaces.items():
        if n == 0:
          continue
        n1 = (n-1)//2
        n2 = (n-1) - n1
        if n1 not in spaces2:
          spaces2[n1] = 0
        spaces2[n1] += count
        if n2 not in spaces2:
          spaces2[n2] = 0
        spaces2[n2] += count
      
      #print spaces2
      spaces = spaces2
      continue

    #print avail
    intervals = spaces.keys()
    intervals.sort()
    while k < K:
      i = intervals.pop()
      c = spaces[i]
      k = min(K, k+c)
      if K == k:
        return (i+1)-(i+1)//2-1, (i+1)//2-1


dataset=open(sys.argv[1], 'r')
T=int(dataset.readline())
for t in xrange(1,T+1):
  (N, K)=map(int, dataset.readline().split())
  max_lsrs, min_lsrs = bathrooms(N,K)
  print "Case #%d: %d %d"%(t, max_lsrs, min_lsrs)
