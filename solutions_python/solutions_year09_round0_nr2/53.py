#!/usr/bin/env python2.3
#
#  geo.py
#  
#
#  Created by Steven Holte on 9/3/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

import sys
import numpy
from numpy import *

f = sys.stdin

T = int(f.readline())

for case in range(T):
  H,W = [int(x) for x in f.readline().split()]
  map = zeros((H,W),'i')
  for h in range(H):
    map[h] = [int(x) for x in f.readline().split()]
  flow = zeros((H,W),'i')
  for r,c in ndindex((H,W)):
    if r<=0:
      north = 999999
    else:
      north = map[r-1,c]
    if c<=0:
      west = 999999
    else:
      west = map[r,c-1]
    if r>=H-1:
      south = 999999
    else:
      south = map[r+1,c]
    if c>=W-1:
      east = 999999
    else:
      east = map[r,c+1]
    flow[r,c] = array([map[r,c], north, west, east, south]).argmin(0)
  sink = zeros((H,W),'i')
  
  seeds=[]
  sinkcount = 0
  for c in range(W):
    for r in range(H):
      if flow[r,c] == 0:
        sinkcount+=1
        seeds.append((r,c))
        sink[r,c]=sinkcount
  
  while len(seeds)>0:
    r,c = seeds.pop()
    if r>0 and sink[r-1,c]==0 and flow[r-1,c]==4:
      sink[r-1,c]=sink[r,c]
      seeds.append((r-1,c))
    if c>0 and sink[r,c-1]==0 and flow[r,c-1]==3:
      sink[r,c-1]=sink[r,c]
      seeds.append((r,c-1))
    if r<H-1 and sink[r+1,c]==0 and flow[r+1,c]==1:
      sink[r+1,c]=sink[r,c]
      seeds.append((r+1,c))
    if c<W-1 and sink[r,c+1]==0 and flow[r,c+1]==2:
      sink[r,c+1]=sink[r,c]
      seeds.append((r,c+1))
  
  print "Case #%s:"%(case+1)
  names = {}
  nextname = 'a'
  for r in range(H):
    for c in range(W):
      if sink[r,c] not in names:
        names[sink[r,c]]=nextname
        nextname = chr(ord(nextname)+1)
      print names[sink[r,c]],
    print
    