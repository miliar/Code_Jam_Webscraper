#!/usr/bin/env python
# =============================================================================
# @file theme.py
# @author Albert Puig Navarro (djkarras@gmail.com)
# @date 08/05/2010
# =============================================================================

import sys
import os

filename = sys.argv[1]
inFile = open(filename)
outFile = open("out.dat", "w") 

T = int(inFile.readline().rstrip('\n'))

for case in xrange(1,T+1):
  R, k, N = [int(val) for val in inFile.readline().rstrip('\n').split()]
  groups = [int(val) for val in inFile.readline().rstrip('\n').split()]
  if len(groups) != N:
    print "problem"
  tot = 0
  for ride in xrange(0, R):
    s = 0
    for i in xrange(1,N+1):
      news = sum(groups[:i])
      if news > k:
        groups = groups[i-1:]+groups[:i-1]
        break
      else:
        s = news
    tot = tot + s
  res = "Case #%s: %s" %(case, tot)
  print res
  outFile.write(res+"\n")
    