#! /usr/bin/python

import sys, string
from sys import argv

def rollerCoaster(R, K, lst):
  index = 0
  result = 0
  for i in xrange(0, R):
    left = K
    start = index
    while lst[index] <= left:
      left = left - lst[index]; index = index + 1;
      if index >= len(lst):
        index = 0
      if index == start:
        break
    result = result + (K - left)
  return result

def nextInt():
  f = open( argv[1], 'r' )
  for line in f.readlines():
    for word in line.split(' '):
      yield int(word)

val = nextInt()
t = val.next()
for i in xrange(0, t):
  R = val.next(); K = val.next(); N = val.next();
  lst = []
  for n in xrange(0, N):
    lst.append(val.next())
  print "Case #%d: %d" % (i + 1, rollerCoaster(R, K, lst))
