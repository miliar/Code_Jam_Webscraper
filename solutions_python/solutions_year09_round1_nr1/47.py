#!/usr/bin/env python

import sys

def representation(n, base):
  if base == 10:
    return str(n)
  if base == 8:
    return oct(n)
  l = []
  while n:
    l.append(str(n % base))
    n /= base
  return ''.join(reversed(l))

def sq(n, base):
  return sum([int(x)**2 for x in representation(n, base)])

def happy(n, base):
  s = set()
  while n != 1:
    if n in s:
      return False
    s.add(n)
    n = sq(n, base)
  return True

def nhappy(n, baselist):
  return all([ happy(n, x) for x in baselist])

def minhappy(baselist):
  n = 2
  while not nhappy(n, baselist):
    n += 1
  return n

f = sys.stdin
N = int(f.readline())
for i in range(1,N+1):
  baselist = [int(x) for x in f.readline().split()]
  print 'Case #%d: %d' % (i, minhappy(baselist))