#!/usr/bin/python
from sys import *

def gcd(a,b):
  while b!=0: b,a = a%b,b
  return abs(a)

c=long(stdin.readline())

for count in range(c):
  nt=map(long,stdin.readline().split())
  nt.pop(0); t0 = nt.pop(0)
  t = map(lambda x: x-t0, nt)
  print 'Case #%d: %d' % (count+1, -t0%reduce( gcd, t, 0 ) )
