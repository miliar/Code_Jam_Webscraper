#!/usr/bin/env python

def square(n):
  sqrt = n ** 0.5
  return abs(int(sqrt + 0.0000001) - sqrt) < 0.000001

def palindrome(n):
  s = str(n)
  for a, b in zip(s, s[::-1]):
    if a != b:
      return False
  return True

for cse in xrange(1, int(raw_input()) + 1):
  line = raw_input().split()
  count = 0
  for i in xrange(int(line[0]), int(line[1]) + 1):
    if square(i) and palindrome(i) and palindrome(int(i ** 0.5 + 0.000001)):
      count += 1
  print 'Case #{}: {}'.format(cse, count)
