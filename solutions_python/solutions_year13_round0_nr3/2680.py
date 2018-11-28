#!/usr/bin/env python

import math

def isPalindrome(s):
  i = 0
  j = len(s) - 1
  while (j > i):
    if (s[j] != s[i]):
      return False
    j -= 1
    i += 1

  return True

def foo(n):
  # print n
  sqrt = int(math.sqrt(n))
  if (sqrt * sqrt != n):
    return False
  if (not isPalindrome(str(sqrt))):
    return False
  s = str(n)
  if (not isPalindrome(s)):
    return False
  # print n
  return True

def fairAndSquare(n):
  vals = f.readline().split()
  vals = [int(s) for s in vals]
  A = vals[0]
  B = vals[1]

  count = 0
  for i in xrange(A, B+1):
    if (foo(i)):
      count += 1
  print "Case #" + str(n) + ": " + str(count)

f = open('C-small-attempt0.in', 'r')
t = int(f.readline())

for i in xrange(0, t):
  fairAndSquare(i+1)
