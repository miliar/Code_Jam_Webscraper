#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin, exit

ts = int(stdin.readline().strip())
for i in range(1, ts+1):
  [x, r, c] = [int(x) for x in stdin.readline().strip().split(' ')]
  n = r * c
  # 1-omino
  if x == 1:
    print "Case #%d: GABRIEL" % i
    continue
  # 2-omino
  if x == 2:
    print "Case #%d: %s" % (i, "GABRIEL" if n % 2 == 0 else "RICHARD")
    continue
  # 3-omino
  if x == 3:
    if (n % 3 != 0) or ((r,c) in [(1,3),(3,1)]):
      print "Case #%d: RICHARD" % i
    else:
      print "Case #%d: GABRIEL" % i
    continue
  # 4-omino
  if x == 4:
    if (n % 4 != 0) or ((r,c) in [(4,1),(1,4),(2,4),(4,2),(2,2)]):
      print "Case #%d: RICHARD" % i
    else:
      print "Case #%d: GABRIEL" % i
    continue
