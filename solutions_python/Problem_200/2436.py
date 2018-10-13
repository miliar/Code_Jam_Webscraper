#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
  sys.exit('usage: ./B.py [input_file]')

with open(sys.argv[1], 'r') as inf:
  lines = inf.readlines()
  n = int(lines[0].strip())
  for i in xrange(1, n+1):
    m = lines[i].strip()
    k = len(m) - 1
    curr_max = m[k]
    while k >= 0:
      while k >= 0 and m[k] <= curr_max:
        curr_max = m[k]
        k -= 1
      if k == -1:
        break

      m = m[:k] + str(int(m[k]) - 1) + '9' * len(m[(k+1):])
      curr_max = m[k]

    if m[0] == '0':
      m = m[1:]

    print 'Case #{0}: {1}'.format(i, m)