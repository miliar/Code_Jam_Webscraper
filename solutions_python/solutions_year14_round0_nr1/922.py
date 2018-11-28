#!/usr/bin/env python

_f = open('in','r')
T = int(_f.readline())

for t in xrange(T):
  cand = [0] * 16
  r1 = int(_f.readline())-1
  for r in xrange(4):
    line = _f.readline()
    if r==r1: 
      for x in line.split():
        cand[int(x)-1] += 1
  r2 = int(_f.readline())-1
  for r in xrange(4):
    line = _f.readline()
    if r==r2:
      for x in line.split():
        cand[int(x)-1] += 1
  result = 0
  tot = 0
  for i in xrange(16):
    if cand[i]==2:
      result = i+1
      tot += 1
  if tot == 1:
    print 'Case #' + str(t+1) + ': ' + str(result)
  elif tot == 0:
    print 'Case #' + str(t+1) + ': Volunteer cheated!'
  else:
    print 'Case #' + str(t+1) + ': Bad magician!'
