#!/usr/bin/python

import sys

results = {}

def test(s,n):
  i = n
  while i > 1:
    try:
      i = s.index(i) + 1
    except:
      return False
  return True

def solve(n):
  if results.has_key(n):
    return results[n] % 100003
  cnt = 0
  for i in range(2**(n-2)):
    s = []
    b = bin(i)[2:].rjust(n-2,'0')
    for j in range(2,n):
      if (b[j-2] == '1'):
        s.append(j)
    s.append(n)
    if test(s,n):
      cnt += 1
  results[n] = cnt
  return cnt % 100003

n = int(sys.stdin.readline())

for i in range(1,n+1):
  n = int(sys.stdin.readline())
  print 'Case #%d:' % i, solve(n)
