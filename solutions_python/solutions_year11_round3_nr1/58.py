#!/usr/bin/env python

"""
Contest: Google Code Jam Round 1C
Problem: 
"""

from decimal import *
getcontext().rounding = ROUND_HALF_UP
import math
import sys


input_file = open(sys.argv[1])

numcases = int(input_file.readline().strip())
for i in xrange(1, numcases+1):
  pattern = dict()
  blues = dict()
  can_convert = True
  fields = input_file.readline().split()
  R, C = int(fields[0]), int(fields[1])
  for r in xrange(0, R):
    row = input_file.readline()
    pattern[r] = dict()
    for c in xrange(0, C):
      pattern[r][c] = row[c]
      if row[c] == '#':
        blues[(r, c)] = True
  for r in xrange(0, R):
    for c in xrange(0, C):
      if pattern[r][c] == '#':
        if (not r == (R-1)) and (not c == (C-1)):
          if (pattern[r][c+1] == '#') and (pattern[r+1][c] == '#') and (pattern[r+1][c+1] == '#'):
            pattern[r][c] = '/'
            pattern[r][c+1] = '\\'
            pattern[r+1][c] = '\\'
            pattern[r+1][c+1] = '/'
            blues[(r, c)] = False
            blues[(r, c+1)] = False
            blues[(r+1, c)] = False
            blues[(r+1, c+1)] = False
  for x in blues.values():
    if x == True:
      can_convert = False
  print("Case #%d:" % i)
  if can_convert == False:
    print("Impossible")
  else:
    for r in xrange(0, R):
      for c in xrange(0, C):
        sys.stdout.write(pattern[r][c])
      sys.stdout.write('\n')
    