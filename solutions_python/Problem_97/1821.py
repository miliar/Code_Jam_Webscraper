#!/bin/python
import os, sys

filename = "C-small-attempt0"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")
T = int(infile.readline())

for index in xrange(T):
  a, b = map(int, infile.readline().split())
  recycled = {}
  for i in xrange(a, b+1):
    s = str(i)
    min_i = i
    for j in xrange(len(s)):
      test_i = int(s)
      if test_i < min_i:
        min_i = test_i
      s = s[-1] + s[:-1]
    count = recycled.get(min_i, 0)
    recycled[min_i] = count + 1

  total = 0
  for v in recycled.itervalues():
    total += (v-1)*v/2

  outfile.write("Case #%d: %d\n" % (index+1, total))

