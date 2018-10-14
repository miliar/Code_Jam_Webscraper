#!/usr/bin/env python
# =============================================================================
# @file snappers.py
# @author Albert Puig Navarro (djkarras@gmail.com)
# @date 08/05/2010
# =============================================================================

import sys
import os

lastONList = [0]
for i in xrange(1,31):
  lastONList.append((lastONList[i-1]*2)+1)

filename = sys.argv[1]
inFile = open(filename)
outFile = open("out.dat", "w") 

T = int(inFile.readline().rstrip('\n'))

for case in xrange(1,T+1):
  N, K = [int(val) for val in inFile.readline().rstrip('\n').split()]
  firstON = lastONList[N]
  if firstON > K:
    state = 'OFF'
  elif firstON == K:
    state = 'ON'
  else:
    ON = firstON
    state = 'OFF'
    while ON < K:
      ON = ON + firstON+1
      if ON==K:
        state = 'ON'
        break
  outFile.write("Case #%s: %s\n" %(case, state))

outFile.close()