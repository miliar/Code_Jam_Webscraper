#!/usr/bin/python

import math

def pal(num):
  s = str(num)
  n = len(s)
  for i in range(n/2):
    if s[i] != s[n-1-i]:
      return False
  return True

n = int(raw_input())

for i in range(n):
  a,b = [int(x) for x in raw_input().split()]

  c = int(math.ceil(math.sqrt(a)))
  count = 0
  while c*c <= b:
    if pal(c) and pal(c*c):
      count += 1
    c += 1
  print "Case #%d: %d" % (i+1, count)
