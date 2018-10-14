#!/usr/bin/env python

T = int(raw_input())
for case in range(T):
  N = int(raw_input())
  vals = [int(c) for c in raw_input().split(' ')]
  xor_all = reduce(lambda a,b: a^b, vals)
  if xor_all:
    print 'Case #%i: NO' % (case+1)
  else:
    print 'Case #%i: %i' % (case+1, sum(vals) - min(vals))
