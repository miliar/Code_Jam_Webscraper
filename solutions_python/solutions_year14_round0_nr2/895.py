#!/usr/bin/env python

_f = open('in','r')
T = int(_f.readline())

for t in xrange(T):
  C,F,X = (float(x) for x in _f.readline().split())
  res = 0.0
  if X <= C:
    print 'Case #' + str(t+1) + ': ' + str(0.5*X)
    continue
  r = 2.0
  res = 0.5 *C
  while F> r*C / (X-C):
    r += F
    res += C/r
  res += (X-C)/r
  print 'Case #' + str(t+1) + ': ' + str(res)
