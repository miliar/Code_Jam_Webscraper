#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(T, i):
  R, C, W = map(int, t[k].split(' '))
  if W == 1:
    print 'Case #%d: %d'%(i, R*C)
    return
  if W == C:
    print 'Case #%d: %d'%(i, C)
    return
  if W >= (C+1)/2:
    print 'Case #%d: %d'%(i, W+1)
    return
  else:
    D = C-W
    miss = 1
    while (D+1)/2 > W:
      miss += 1
      D -= W
    print 'Case #%d: %d'%(i, miss+W+1)

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t[k], k+1)
