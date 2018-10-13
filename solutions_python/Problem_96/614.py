#!/usr/bin/env python

import sys

t = int(raw_input())

for i in range(t):
  l = [ int(x) for x in raw_input().split(' ') ]
  n, s, p = l[0:3]
  l = l[3:]
  l.sort()
  res = 0
  for j in range(len(l) - 1, -1, -1):
    if p + max(2 * (p - 1), 0) <= l[j]:
      res += 1
    elif s > 0:
      if p + max(2 * (p - 2), 0) <= l[j]:
        res += 1
        s -= 1
      else:
        break
    else:
      break
  print 'Case #%d: %d' % (i + 1, res)
