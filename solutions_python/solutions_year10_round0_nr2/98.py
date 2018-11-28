#!/usr/bin/env python

from sys import stdin

def gcd(a, b):
   if a < 0: a = -a
   if b < 0: b = -b
   if a < b:
      a, b = b, a
   while b > 0:
      t = b
      b = a % b
      a = t
   if a > 0:
      return a
   else:
      return 1


TC = int(stdin.readline().strip())
for tc in xrange(1, TC+1):
   a = map(int, stdin.readline().split())
#  N = a[0]

#  uniques = {}
#  for i in xrange(1,len(a)):
#     uniques[ a[i] ] = 1
#  t = uniques.keys()
   t = list( set(a[1:]) )

#  print len(t)

   T = abs(t[0]-t[1])
   for i in xrange(len(t)):
      for j in xrange(i+1, len(t)):
         T = gcd(T, t[i]-t[j])

#  print 'T=', T

   m = (t[1]+T-1)/T
   res = m * T - t[1]
   print 'Case #%d: %d' % (tc, res)
