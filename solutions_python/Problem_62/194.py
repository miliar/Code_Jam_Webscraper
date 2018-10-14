#!/usr/bin/python

import sys

def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
  d = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
  if d == 0.0: return False
  ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / d
  ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / d
  if ua > 1.0 or ua < 0.0: return False
  if ub > 1.0 or ub < 0.0: return False
  return True

def solve(n):
  cnt = 0
  l = []
  for i in range(n):
    l.append( map(float,sys.stdin.readline().split(' ')) )
  for i in range(len(l)):
    for j in range(i):
      if intersect(l[i][0],0.0,l[i][1],1.0,l[j][0],0.0,l[j][1],1.0):
        cnt += 1
  return cnt

t = int(sys.stdin.readline())

for i in range(1,t+1):
  n = int(sys.stdin.readline())
  print 'Case #%d:' % i, solve(n)
