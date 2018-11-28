#!/usr/bin/env python

import sys, re, time

try:
  f = open(sys.argv[1])
except IOError:
  print "No input file specify, do nothing."
  exit()

def can_cut(data, i, j):
  t = zip(*data)
  cur_h = data[i][j]
  rp = rq = True
  for p in data[i]:
    if p > cur_h:
      rp = False
      break
  for q in t[j]:
    if q > cur_h:
      rq = False
      break

  return rp or rq

def _solve(data):
  for i,iv in enumerate(data):
    for j,jv in enumerate(iv):
      r = can_cut(data, i, j)
      if r is False:
        return False

  return True

def solve(data):
  r = _solve(data)

  return 'YES' if r else 'NO'

n = int(f.readline())
for i in range(n):
  x,y = f.readline().strip().split(' ')
  x = int(x)
  y = int(y)
  data = [[int(l) for l in f.readline().strip().split(' ')] for k in range(x)]
  print "Case #%d: %s" % (i + 1, solve(data))
