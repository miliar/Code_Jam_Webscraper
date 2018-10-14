#!/usr/bin/env python

import sys
from math import floor, ceil, sqrt
import ipdb

def palindrome(i):
  return (str(i) == str(i)[::-1])

def calc(a,b):
  count = 0
  for i in xrange(int(floor(sqrt(a)))-1, int(ceil(sqrt(b)))+1):
    if palindrome(i):
      if palindrome(pow(i,2)):
        if pow(i,2) >= a and pow(i,2) <= b:
          #print "Found: " + str(i) + " square: " + str(pow(i,2))
          count += 1
  return str(count)





ifile = open(sys.argv[1])
if len(sys.argv) > 2:
  ofile = open(sys.argv[2])
else:
  ofile = sys.stdout
for i in range(int(ifile.readline().strip())):
  a, b = map(lambda x:int(x), ifile.readline().strip().split(' '))
  print "Case #%i: %s" % (i+1, calc(a,b))
