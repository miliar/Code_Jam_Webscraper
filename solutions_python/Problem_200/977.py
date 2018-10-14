#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random
import heapq

def is_tidy(n):
  digits = list(str(n))
  return digits == sorted(digits)

def slow_solve(n):

  if n > 1000:
    return 0

  i = n
  while not is_tidy(i):
      i -=1
  return i

def solve(n):

  digits = [int(x) for x in list(str(n))]
  #print digits

  i = len(digits) -1
  while i > 0:
    if digits[i] < digits[i-1]:
      digits[i-1] -= 1
      for j in range(i, len(digits)):
        digits[j] = 9
    i -= 1
    #print digits
  return int("".join([str(x) for x in digits]))



total = None
count = 0
f = sys.stdin

count = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  else:
    tests.append(int(line.strip()))

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for n in tests:
  counter += 1
  #print t
  print "Case #%d: %d" % (counter, solve(n))
  #sys.exit()



