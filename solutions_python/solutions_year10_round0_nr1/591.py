#!/usr/bin/env python

ans = ['OFF', 'ON']
for t in xrange(input()):
   n,k = (int(x) for x in raw_input().split())
   print "Case #%d:"%(t+1), ans[bin(k)[-n:].count('1')/n]
