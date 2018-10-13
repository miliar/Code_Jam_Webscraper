#!/usr/bin/env python 
# -*- coding: iso-8859-1 -*-
import os
import sys

  
  
def func(n, k):
  allSet = (2 ** n)-1
  if (allSet & k) == allSet:
      return "ON"
  return "OFF"

  
def main():
  #f = open('A-test.in')
  #f = open('A-small-attempt0.in')
  f = open('A-large.in')
  n = int(f.readline().strip())
  values = []
  for i in range(n):
    value = [int(i) for i in f.readline().split()]
    values.append(value)
    
  for i in range(n):
    print 'Case #%s: %s' % (i+1, func(*values[i]))

  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
