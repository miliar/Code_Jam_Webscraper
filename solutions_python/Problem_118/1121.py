#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import math
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def is_palindrome(x):
  return str(x) == str(x)[::-1]

def challenge():
  A, B = map(int, getline().split());
  A_root = int(math.ceil(A**.5))
  B_root = int(math.floor(B**.5))

  fair_and_square = 0
  for x in xrange(A_root, B_root + 1):
    if is_palindrome(x) and is_palindrome(x**2):
      fair_and_square += 1

  print fair_and_square

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

