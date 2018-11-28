#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random
import math

def solve(r, x):
  #print r
  #print x
  made = 0

  x_new = []

  for i in xrange(len(r)):
    next = []
    for p in x[i]:
      z = float(p) / r[i]
      up = int(math.floor(z/0.9))
      down = int(math.ceil(z/1.1))
      if up >= down:
        next.append((down, up))
    if len(next) == 0:
      return 0
    x_new.append(sorted(next))

  x = x_new
  #print x

  indices = [0 for j in xrange(len(r))]
  while(True):
    #print indices
    mn, mx = x[0][indices[0]]
    #print mn, mx
    match = True
    for i in range(len(r)):
      while indices[i] < len(x[i]) and x[i][indices[i]][1] < mn:
        indices[i] += 1
      if indices[i] == len(x[i]):
        return made
      if x[i][indices[i]][0] > mx:
        match = False
        mn = x[i][indices[i]][0]
      
    if match:
      made += 1
      for i in range(len(r)):
        indices[i] += 1
        if indices[i] == len(x[i]):
          return made
    else:
      for i in range(len(r)):
        while indices[i] < len(x[i]) and x[i][indices[i]][1] < mn:
          indices[i] += 1
        if indices[i] == len(x[i]):
          return made
        
  return made

total = None
count = 0
f = sys.stdin

count = None
n, p = None, None
r = None
next = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  elif n == None:
    n, p = [int(x) for x in line.strip().split()]
    next = []
  elif r == None:
    r = [int(x) for x in line.strip().split()]
  else:
    next.append(sorted([int(x) for x in line.strip().split()]))
    if len(next) == n:
      tests.append((r, next))
      n, p = None, None
      r = None
      next = []

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for r, x in tests:
  counter += 1
  #print t
  print "Case #%d: %s" % (counter, solve(r, x))
  #sys.exit()

