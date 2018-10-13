#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random
import heapq

def solve(n, k):
  #print n, k

  intervals = [-n,]
  interval_counts = {n:1}  
  
  for i in xrange(k):
    #print i, k-1, intervals
    longest = -heapq.heappop(intervals)
    x = (longest /2, longest/2 - (1 if longest %2 == 0 else 0))
    number = interval_counts[longest]
    if number >= k:
      return x

    for y in x:
      if y not in interval_counts:
        heapq.heappush(intervals, -y)
        interval_counts[y] = 0
      interval_counts[y] += number
    k -= number

  #print i
  assert False

total = None
count = 0
f = sys.stdin

count = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  else:
    tests.append([int(x) for x in line.strip().split()])

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for n, k in tests:
  counter += 1
  #print t
  s = solve(n, k)
  print "Case #%d: %s %s" % (counter, s[0], s[1])
  #sys.exit()



