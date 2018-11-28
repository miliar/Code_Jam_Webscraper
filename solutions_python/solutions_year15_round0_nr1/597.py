#!/bin/env python

cases = int(raw_input())

for i in xrange(cases):
  people = map(int, raw_input().split()[-1])
  total = 0
  added = 0
  for ind, num in enumerate(people, 0):
    if total < ind:
      diff = ind - total
      added += diff
      total += diff
    total += num
  print 'Case #{}: {}'.format(i+1, added)

