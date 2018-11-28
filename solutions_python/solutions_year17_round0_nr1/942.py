#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

limit = 10000


def solve(s, k):
  #print s, k
  if len(s) < k:
    for c in s:
      if c == "-":
        return None
    return 0

  flipped = 0
  if s[0] == "-":
    for i in range(k):
      if s[i] == "-": s[i] = "+"
      elif s[i] == "+": s[i] = "-"
    flipped = 1

  result = solve(s[1:], k)
  if result is not None:
    return result + flipped
  return None

  print s, "escape"
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
    t = line.strip().split()
    tests.append((list(t[0]), int(t[1])))

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for s, k in tests:
  counter += 1
  #print t
  result = solve(s, k)
  print "Case #%d: %s" % (counter, "IMPOSSIBLE" if result == None else str(result))
  #sys.exit()



