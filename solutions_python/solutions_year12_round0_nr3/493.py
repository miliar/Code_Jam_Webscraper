#!/usr/bin/env python

def shift(item, value):
  last = item % 10
  return item / 10 + value * last

def solve(lst):
  total = 0
  A = int(lst[0])
  B = int(lst[1])
  order = len(lst[0]) - 1
  value = 10 ** order
  for curr in xrange(A,B + 1):
    tmp = shift(curr, value)
    while tmp != curr:
      if tmp < curr and tmp >= A:
        total += 1
      tmp = shift(tmp, value)
  return total


num_of_cases = int(raw_input())

num = 1

while num <= num_of_cases:
  case = raw_input().split()
  print "Case #" + str(num) + ": " + str(solve(case))
  num += 1
