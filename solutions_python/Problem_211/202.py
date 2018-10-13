#!/usr/bin/env python

import math 

def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)

def dictadd(dct, key, val):
  if not dct.has_key(key):
    dct[key] = val
  else:
    dct[key] += val  
  
def call():
  n, k = [int(i) for i in raw_input().split()]
  u = float(raw_input())
  data1 = [float(i) for i in raw_input().split(' ')]
  data = {1.0:0}
  for i in data1:
    dictadd(data, i, 1)
  while u > 0.0 and len(data.keys()) != 1:
    m1,m2 = (sorted(data.keys()))[:2]
    diff = data[m1]*(m2 - m1)
    if data[m1]*(m2 - m1) > u:
      count = data[m1]
      del data[m1]
      data[m1 + u / count] = count
      u = 0.0
    else:
      count = data[m1]
      del data[m1]
      data[m2] += count
      u -= diff
  m = 1
  for i in data:
    m *= i**data[i]
  return m
  
    
  
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call())