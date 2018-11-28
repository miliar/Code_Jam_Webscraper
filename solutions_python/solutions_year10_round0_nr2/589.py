#!/usr/bin/python
import sys

f = sys.stdin
C = int(f.readline())

def gcd (a,b):
  if b == 0: return a
  else: return gcd(b, a%b)

for case in xrange(1, C+1):
  s = f.readline().split()
  N = int(s[0])
  t = [int(x) for x in s[1:]]
  del s
  m = min(t)
  d = [x - m for x in t if x > m]
  for i in xrange(0,len(d)-1):
    d[i+1] = gcd(d[i],d[i+1])
  T = d[-1]
  m = m % T
  if m == 0: print 'Case #%d:' % case, 0
  else: print 'Case #%d:' % case, T - m

