#!/usr/bin/env python

import sys
sys.setrecursionlimit(10000000)

INF = 1000000000000

def last1(s):
  p = 0
  for i in xrange(len(s)):
    if s[i] == '1':
      p = i
  return p

def done(num):
  for i, n in enumerate(num):
    if n > i:
      return False
  return True

def solve(num, sofar = 0):
  global seen
  if done(num):
    return 0
  tnum = tuple(num)
  if tnum in seen and seen[tnum] >= sofar:
    return INF
  seen[tnum] = sofar
  ans = INF
  for i, row in enumerate(num):
    if i > 0 and num[i] < num[i-1]:
      num[i], num[i-1] = num[i-1], num[i]
      ans = min(ans, solve(num, sofar+1)+1)
      num[i], num[i-1] = num[i-1], num[i]
  return ans

for case in xrange(1, int(raw_input())+1):
  N = int(raw_input())
  num = [last1(raw_input()) for _ in xrange(N)]
  seen = {}
  print "Case #%d: %d" % (case, solve(num))
