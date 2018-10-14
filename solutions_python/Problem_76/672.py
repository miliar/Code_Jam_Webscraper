#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import copy

def subset(a):
  for n in range(2**len(a)):
    yield [a[i] for i in xrange(len(a)) if (n >> i) & 1 == 1]

def calc_xor(data):
  res = 0
  for d in data:
    res ^= d
  return res

def subdata(data, subs):
  res = copy.deepcopy(data)
  for s in subs:
    if s in data:
      res.remove(s)
  return res

case = int(sys.stdin.readline())
for c in range(0, case):
  candy_num = sys.stdin.readline()
  candies = [int(item) for item in sys.stdin.readline().strip().split()]

  result = -1
  for s1 in subset(candies):    
    s2 = subdata(candies, s1)
    if len(s1) == 0 or len(s2) == 0:
      continue
    
    val1 = calc_xor(s1)
    val2 = calc_xor(s2)

    if val1 == val2:
      real = sum(s1)
      if real > result:
        result = real

  ans = 'NO' if result < 0 else result
  print "Case #%d: %s" % (c+1, ans)
