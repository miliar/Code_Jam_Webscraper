#!/usr/bin/python

import sys
import numpy

def isPal(num):
  digits = numpy.log10(num) + 1
  if digits == 1: return True
  stack = []
  while num > 0:
    stack.append(num % 10)
    num //= 10
  
  return stack == stack[::-1]

def isSq(num):
  squre = numpy.sqrt(num)
  return squre % 1 == 0.0, squre

def checkNum(num):
  chckSq, sqNum = isSq(num)
  if not chckSq: return 0
  if not isPal(num): return 0
  if not isPal(sqNum): return 0
  return 1
  
if __name__ == '__main__':
  
  filename = sys.argv[1];
  
  with open(filename) as f:
    total = int(f.readline())
    for i in range(0,total):
      start, end = (f.readline()).split()
      start = int(start)
      end = int(end)
      found = 0
      for x in range(start,end+1):
        found += checkNum(x)
      
      print "Case #%d: %d" % (i+1,found)
      
      