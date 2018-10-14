#!/usr/bin/env python

import sys, re, time, math

try:
  f = open(sys.argv[1])
except IOError:
  print "No input file specify, do nothing."
  exit()

def is_pal(x):
  xs = str(x)
  return xs == xs[::-1]

def is_sqr(x):
  xsqrt = math.sqrt(x)
  return xsqrt == float(int(xsqrt)) and is_pal(int(xsqrt))

def find_fair_sqr(a, b):
  count = 0
  for i in xrange(a, b+1):
    if is_pal(i) and is_sqr(i):
      count += 1
  return count

n = int(f.readline())
for i in range(n):
  a,b = f.readline().strip().split(' ')
  a,b = [int(a),int(b)]
  print "Case #%d: %d" % (i+1, find_fair_sqr(a, b))
