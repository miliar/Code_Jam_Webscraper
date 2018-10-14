#!/usr/bin/python

import sys

def foo(n,k):
  if bin(k)[-n:] == n*'1':
    return 'ON'
  else:
    return 'OFF'

t = int(sys.stdin.readline())

for i in range(1,t+1):
  (n,k) = map(int,sys.stdin.readline().split(' '))
  print 'Case #%d:' % i, foo(n,k)
