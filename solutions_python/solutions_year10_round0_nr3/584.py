#!/usr/bin/env python

for t in xrange(input()):
  r,k,n = (int(x) for x in raw_input().split())
  l = [int(x) for x in raw_input().split()]
  s = sum(l)
  if (s<=k):
    print "Case #%d:"%(t+1), r*s
  else:
    cache = {}
    i = 0
    while True:
      try:
        if (cache[i]>0):
          break
      except KeyError:
        cache[i] = [0,0]
        j = i
        while (cache[i][0] + l[j] <= k):
          cache[i][0] += l[j]
          j = (j+1) % n

        #print "from %d to %d i got this" % (i,(j-1)%n)
        cache[i][1]=j
        i=j

    i=0   # hop
    j=0   # money
    for x in xrange(r):
      j += cache[i][0]
      i = cache[i][1]
    print "Case #%d:"%(t+1), j





