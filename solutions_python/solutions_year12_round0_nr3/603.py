#!/usr/bin/env python

import sys

def check_number(x, a, b, n):
  t = x
  res = 0
  s = set()
  for i in range(n - 1):
    t = (t % 10) * 10**(n - 1) + t / 10
    if t > x and t <= b and t not in s:
      s.add(t)
      res += 1
  return res

t = int(raw_input())

for i in range(t):
  a, b = raw_input().strip().split(' ')
  n = len(a)
  a = int(a)
  b = int(b)
  res = 0
  for j in range(a, b):
    res += check_number(j, a, b, n)
  print 'Case #%d: %d' % (i + 1, res)
