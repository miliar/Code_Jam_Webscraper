#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def find_last(D, KS):
  t = 0.
  for k, s in KS:
    new_t = (D-k)/s
    if new_t > t:
      t = new_t
  return D/t

def solve(D, KS, i):
  v = find_last(D, KS)
  print 'Case #%d: %s'%(i, v)

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  if t[-1] == '':
    t = t[:-1]
  k = 0
  i = 1
  while k < len(t):
    D, N = map(int, t[k].split(' '))
    KS = []
    k += 1
    for l in xrange(0, N):
      KS.append(map(float, t[k+l].split(' ')))
    solve(D, KS, i)
    i+=1
    k += N
