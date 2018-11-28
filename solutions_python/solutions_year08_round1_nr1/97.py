#!/usr/bin/env python2.5

import sys
from math import floor, pi, sqrt
infile = open(sys.argv[1], 'rb')
numcases = int(infile.readline())

for case in xrange(1, numcases+1):
  vlen = int(infile.readline())
  v1 = [int (v) for v in infile.readline().split()]
  v2 = [int (v) for v in infile.readline().split()]
  
  v1.sort()
  v2.sort(reverse=True)
  
  sum = 0
  for i in xrange(0, len(v1)):
    sum += v1[i]*v2[i]
    
  print "Case #%d: %d" % (case, sum)