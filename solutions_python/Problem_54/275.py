#!/usr/bin/python3

from fractions import gcd
from functools import reduce

t = int(input())

for c in range(1, t + 1):
  n, *a = input().split(' ')
  n, a, b = int(n), [int(q) for q in a], int(a[0])
  a = [abs(p-q) for p in a for q in a]
  g = reduce(lambda x, y: gcd(x,y), a)
  print('Case #%d: %s' % (c, (-b) % g))
  
