#!/usr/bin/env python

"""
Contest: Gpogle Code Jam Qualification Round
Problem: Bot Trust
"""

import math
import sys

"""=================
INIT DATA STRUCTURES
================="""
o_pos = 1
b_pos = 1
o_buttons = []
b_buttons = []
timer = 0

"""=================
PARSE INPUT + SET UP
================="""
input_file = open(sys.argv[1])
numcases = int(input_file.readline().strip())
for i in xrange(1, numcases+1):
  fields = input_file.readline().split()
  numbuttons = int(fields[0])
  timer = 0
  opos = 1
  bpos = 1
  oaccum = 0
  baccum = 0
  for j in xrange(1, numbuttons*2 + 1, 2):
    if fields[j] == 'O':
      target = int(fields[j+1])
      to_travel = math.fabs(target - opos)
      if baccum >= to_travel:
        to_travel = 0
      else:
        to_travel -= baccum
      baccum = 0
      to_expend = to_travel + 1
      oaccum += to_expend
      timer += to_expend
      opos = target
    else:
      target = int(fields[j+1])
      to_travel = math.fabs(target - bpos)
      if oaccum >= to_travel:
        to_travel = 0
      else:
        to_travel -= oaccum
      oaccum = 0
      to_expend = to_travel + 1
      baccum += to_expend
      timer += to_expend
      bpos = target
  print("Case #%d: %d" % (i, timer))

