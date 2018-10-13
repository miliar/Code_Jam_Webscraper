#!/usr/bin/env python2.5

import sys
from math import floor, pi, sqrt
infile = open(sys.argv[1], 'rb')
numcases = int(infile.readline())

for case in xrange(1, numcases+1):
  pkl = infile.readline().split()
  p = int(pkl[0])
  k = int(pkl[1])
  l = int(pkl[2])
  letters = [int(i) for i in infile.readline().split()]

  if p*k < l:
    print "Case #%d: Impossible" % (case)
    continue
  
  letters.sort(reverse=True)
  s = 0
  i = 0
  for l in letters:
    s += l*(1 + i/k)
    i += 1

  print "Case #%d: %d" % (case, s)