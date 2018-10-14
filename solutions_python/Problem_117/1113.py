#! /usr/bin/env python

import numpy as np


def readField(file, N, M):
  field = np.array([[int(c) for c in f.readline().split() if c != ' '] for x in range(0, N)])
  maxrow = []
  maxcol = []
  for n in range(0,N):
    maxrow.append(max(field[n,:]))
  for m in range(0,M):
    maxcol.append(max(field[:,m]))
  return field, maxrow, maxcol


def evalField(field, maxrow, maxcol):
  for n in range(0, len(maxrow)):
    for m in range(0, len(maxcol)):
      if field[n,m] < maxrow[n] and field[n,m] < maxcol[m]:
        return "NO"
  return "YES"


#
# MAIN FUNCTION
#

# open input
with open('B-large.in', 'r') as f:
  numberCases = f.readline().strip()

  for i in range(0, int(numberCases)):
    [N, M] = [int(x) for x in f.readline().split()]
    field, maxrow, maxcol = readField(f, int(N), int(M))
    print "Case #" + str(i+1) + ": " + evalField(field, maxrow, maxcol)