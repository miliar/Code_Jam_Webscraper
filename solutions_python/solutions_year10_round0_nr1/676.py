#!/usr/bin/python

for i in xrange(1, input() + 1):
  (n, k) = map(int, raw_input().split())
  if k % (1 << n) == (1 << n) - 1:
    print "Case #%d: ON" % i
  else:
    print "Case #%d: OFF" % i
