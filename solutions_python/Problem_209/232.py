#!/usr/bin/env python

import math 

def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)
  
def tr(k, p1, index, other):
  s = [i[0]*i[1] for ind, i in enumerate(other) if p1[0] >= i[0] and ind != index]
  if len(s) < k-1:
    return -1
  s.sort()
  s.reverse()
  m = 2*sum(s[:k-1])
  return m
  
def call():
  n, k = [int(i) for i in raw_input().split()]
  data = [[int(j) for j in raw_input().split()] for i in xrange(n)]
  maxval = 0
  for i, j in enumerate(data):
    val = j[0]**2 + 2*j[0]*j[1]
    val += tr(k, j, i, data)
    maxval = max(maxval, val)
  return maxval * math.pi
  
    
  
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call())