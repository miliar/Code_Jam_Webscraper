#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin

ts = int(stdin.readline().strip())
for i in range(1,ts+1):
  ln = stdin.readline().strip().split(' ')
  mx, s = ln[0], ln[1]
  needed, total, missing = 0, 0, 0
  for x in s:
    ppl = int(x)
    if ppl > 0 and needed > total:
      dx = needed - total
      missing += dx
      total += dx
    total += ppl
    needed += 1
  print "Case #%d: %d" % (i, missing)
