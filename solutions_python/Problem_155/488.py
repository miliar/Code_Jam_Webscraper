#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

count = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  else:
    num, levels = tuple(line.strip().split(" "))
    num = int(num)
    levels = [int(x) for x in levels]
    #print levels
    if num +1 != len(levels):
      print "Wrong number of levels on line:", line
      sys.exit(0)
    tests.append(levels)

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)


index = 0
for t in tests:
  index += 1
  added = 0
  standing = t[0]
  #print ""
  #print index, added, standing, t
  for i in range(1, len(t)):
    #print i, t[i], standing, added
    if i > standing and t[i] > 0:
      to_add = i - standing
      added += to_add
      standing += to_add + t[i]
    else:
      standing += t[i]
      

  print "Case #%d: %d" % (index, added)
    
