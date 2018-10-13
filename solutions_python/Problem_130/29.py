#!/usr/bin/env python

from sys import argv

f = open(argv[1])
T = int(f.readline().strip())
for tc in xrange(1, T+1):
  N, P = map(int, f.readline().strip().split(' '))
  M = 1 << N
  u = 1
  while (1 << u) <= P:
    u += 1
  u -= 1
  a = M - (1 << (N-u))
  if P == M:
    b = M - 1
  else:
    v = N - 1
    while M - (1 << v) + 1 <= P:
      v -= 1
    v += 1
    b = (1 << (N-v+1)) - 2
  print "Case #%d: %d %d" % (tc, b, a)

