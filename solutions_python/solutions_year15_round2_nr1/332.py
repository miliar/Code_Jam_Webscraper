#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

N = 10 ** 6 + 1
min_counts = [N] * (N)

min_counts[1] = 1

def flip(n):
  return int(str(n)[::-1])

for i in xrange(2, len(min_counts)):
  min_counts[i] = min(min_counts[i-1] + 1, min_counts[i])
  f = flip(i)
  min_counts[f] = min(min_counts[i] + 1, min_counts[f])

#print min_counts

def c(n):
  return min_counts[n] if n < N else -1

def solve(f):
  #parse
  num = int(f.readline().strip())
  return c(num)

total = None
count = 0
f = sys.stdin
while f:
  if not total:
    total = int(f.readline().strip())
    continue
  elif count < total:
    count += 1
    print "Case #%d: %s" % (count, solve(f))
  else:
    break

if count < total:
  print "Wrong number of test cases"
  sys.exit(0)

