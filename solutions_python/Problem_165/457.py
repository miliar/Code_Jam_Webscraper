#!/usr/bin/env python

from sys import stdin
from math import ceil

cases = int(stdin.readline().strip())

for c in range(cases):
  v = stdin.readline().strip().split()
  #print v
  R = int(v[0]); C = int(v[1]); W = int(v[2])

  if W == 1:
    res = R*C
  else:
    #res = int(C/W)*R + W-1 + ( (C-(int(C/W))*W) if W-C%W != 1 else 1 )
    res = W + ceil((float(C)-W)/W)

  print "Case #%d: %d" %(c+1, res)
