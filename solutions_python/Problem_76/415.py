#!/usr/bin/env python2.7

from operator import xor

cases = int(raw_input())

for case in range(cases):
  N = int(raw_input())
  values = [int(n) for n in raw_input().split()]

  if reduce(xor, values) != 0:
    print "Case #%d: NO" % (case + 1)

  else:
    smallest = min(values)
    print "Case #%d: %d" % (case + 1, sum(values) - smallest)
