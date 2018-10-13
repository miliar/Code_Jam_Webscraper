#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def get_all(table, N, w):
  if N == 0:
    return
  if N == 1:
    if (0, 0) in table:
      table[(0, 0)] += w
    else:
      table[(0, 0)] = w
    return
  if N == 2:
    if (1, 0) in table:
      table[(1, 0)] += w
    else:
      table[(1, 0)] = w
    if (0, 0) in table:
      table[(0, 0)] += w
    else:
      table[(0, 0)] = w
    return
  if N == 3:
    if (1, 1) in table:
      table[(1, 1)] += w
    else:
      table[(1, 1)] = w
    if (0, 0) in table:
      table[(0, 0)] += 2*w
    else:
      table[(0, 0)] = 2*w
    return
  if N%2 == 1:
    if (N/2, N/2) in table:
      table[(N/2, N/2)] += w
    else:
      table[(N/2, N/2)] = w
    get_all(table, N/2, 2*w)
  else:
    if (N/2, N/2-1) in table:
      table[(N/2, N/2-1)] += w
    else:
      table[(N/2, N/2-1)] = w
    get_all(table, N/2-1, w)
    get_all(table, N/2, w)

def get_min_max(table, k):
  i = 0
  acc = table[0][1]
  while i < (len(table)-1) and acc < k:
    i += 1
    acc += table[i][1]
  return table[i][0]

def sort_table(t):
  return sorted(t.items(), key=lambda x:x[0], reverse=True)
  
def solve(t, i):
  N, K = map(int, t[i].split(' '))
  table = {}
  get_all(table, N, 1)
  table = sort_table(table)
  a, b = get_min_max(table, K)
  print 'Case #%d: %d %d'%(i+1, a, b)

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t, k)
