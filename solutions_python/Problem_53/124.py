#!/usr/bin/python

t = int(raw_input())

for c in range(1, t + 1):
  n, k = raw_input().split(' ')
  n, k = int(n), int(k)
  res = 'ON' if (k + 1) & ((1 << n) - 1) == 0 else 'OFF'
  print 'Case #%d: %s' % (c, res)
  
