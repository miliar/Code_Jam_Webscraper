#!/usr/bin/env python
import sys

def calc(n, X, F, C):
  a = X/(2+n*F)
  b = 0.0
  for i in range(n):
    b += C / (2+(i*F))
  return a+b

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
  case = i+1
  C, F, X = map(float,rl().split())
  old = calc(0, X, F, C)
  new = calc(1, X, F, C) 
  j = 2
  while new < old:
    old = new
    new = calc(j, X, F, C)
    j += 1
  print 'Case #%d: %.7f' % (case, old)
