#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
  sys.exit('usage: ./A.py [input_file]')

with open(sys.argv[1], 'r') as inf:
  lines = inf.readlines()
  n = int(lines[0].strip())
  for i in xrange(1, n+1):
    cakes, k = lines[i].strip().split()
    k = int(k)

    j = 0
    flag = False
    count = 0
    while j <= len(cakes) - k:
      while j < len(cakes) and cakes[j] == '+':
        j += 1
      if j == len(cakes):
        flag = True
        break
      if j > len(cakes) - k:
        break
      cakes = cakes[:j] + ''.join(['+' if cakes[x] == '-' else '-' for x in xrange(j, j + k)]) + cakes[(j+k):]
      count += 1

    if flag:
      print 'Case #{0}: {1}'.format(i, count)
    else:
      print 'Case #{0}: IMPOSSIBLE'.format(i)
