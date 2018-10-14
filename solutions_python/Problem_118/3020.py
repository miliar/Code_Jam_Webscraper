#!/usr/bin/python

import sys

found = set()

def fairsquare(a,b):
  c = 0
  for i in xrange(a,b+1):
    if i in found:
      c += 1
      continue
    sq = i**0.5
    if sq % 1 == 0 and is_palin(i) and is_palin(sq):
      c += 1
      found.add(i)
  return c

def is_palin(x):
  s = str(int(x))
  if s == s[::-1]:
    return 1
  return 0

n_cases = int(sys.stdin.readline().strip())
curr_case = 1

while curr_case <= n_cases:
  a, b = sys.stdin.readline().strip().split()
  print 'Case #%s: %s' % (curr_case, fairsquare(int(a),int(b)))
  curr_case += 1
