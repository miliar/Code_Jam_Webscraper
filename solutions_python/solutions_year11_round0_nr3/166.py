#!/usr/bin/env python

from sys import stdin

TC = int(stdin.readline().strip())
for tc in xrange(1, TC+1):
   N = int(stdin.readline().strip())
   A = map(int, stdin.readline().split())
   m = 0
   for x in A:
      m ^= x
   print 'Case #%d:' % (tc),
   if m == 0:
      print sum(A) - min(A)
   else:
      print 'NO'
