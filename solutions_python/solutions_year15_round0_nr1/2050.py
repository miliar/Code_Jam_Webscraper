#!/usr/bin/python -tt

import numpy
import re
import sys
import string


f = open(sys.argv[1], 'r+')

n = int(f.readline())
for i in range(n):
  line = f.readline().strip()
  m = int(line.split(' ')[0])
  if m == 0:
    print "Case #{}: {}".format(i + 1, 0)
    continue

  raw = line.split(' ')[1]

  shyness = []
  for j, s in enumerate(raw):
    s = int(s)
    shyness.append(s)

  su = 0
  invi = 0
  for j in range(len(shyness)):
    if su < j:
      invi = invi + (j - su)
      su = su + (j - su)

    su += shyness[j]

  print "Case #{}: {}".format(i + 1, invi)
