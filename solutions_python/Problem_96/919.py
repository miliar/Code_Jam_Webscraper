#!/usr/bin/env python

import sys

def do_case(f):
  info = [int(x) for x in f.readline().split()]
  num_googlers = info[0]
  num_surp = info[1]
  p = info[2]
  count = 0
  for x in info[3::]:
    if p == 0:
      count+=1
    elif (p == 1) and (x < 1):
      count = count
    elif x >= 3*p - 2:
      count+=1
    elif (x >= 3*p - 4) and (num_surp > 0):
      count+=1
      num_surp-=1
  return count

f = sys.stdin
T = int(f.readline())
for i in xrange(T):
  v = do_case(f)
  print "Case #%d: %d" % (i+1, v)