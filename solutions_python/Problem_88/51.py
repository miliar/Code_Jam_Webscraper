#! /usr/bin/python

import sys
from math import sqrt
from decimal import *
getcontext().prec = 100

def check_middle(m, s, x, y):
  mass = [0, 0]

  middle = (s+1) / 2.0 - 1

  for i in range(0, s):
    if i == 0 or i == s-1:
      min_j = 1
      max_j = s-1
    else:
      min_j = 0
      max_j = s
    for j in range(min_j, max_j):
      mass[0] += m[x+i][y+j] * (i - middle)
      mass[1] += m[x+i][y+j] * (j - middle)

  if mass[0] == 0 and mass[1] == 0:
    return True

  return False

def solve(r, c, d, m):

#  print r, c, m

  max_size = min(r, c)

  for b in range(max_size, 2, -1):
#    print b
    for i in range(0, r-b+1):
      for j in range(0, c-b+1):
#        print b, i, j
        if check_middle(m, b, i, j):
          return b

  return "IMPOSSIBLE"
      
fd = open(sys.argv[1])
num_cases = int(fd.readline())

for i in range(0, num_cases):
  (r, c, d) = [int(item) for item in fd.readline().split(" ")]

  m = []
  for j in xrange(r):
    m_tmp = []
    for k in fd.readline().split()[0]:
      m_tmp.append(float(k) + d)
    
    m.append(m_tmp)

  print "Case #%d:" % (i+1), solve(r, c, d, m)
