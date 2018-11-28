#!/usr/bin/env python

###################################################
#
# Google Code Jam File
#
#     python script.py < input.in > output.out
#
###################################################

import sys,string
from math import *

for case in xrange(int(sys.stdin.readline())):
  #var1,var2.var3 = map(int,sys.stdin.readline().strip().split())
  n, A, B, C, D, x0, y0, M = map(int,sys.stdin.readline().strip().split())
  
  x,y = x0,y0
  trees = [(x0,y0)]
  for i in xrange(1,n):
    x,y = (A*x + B) % M,(C*y + D) % M
    trees.append((x,y))
  
  result = 0
  for i in xrange(len(trees)-2):
    for j in xrange(i+1,len(trees)-1):
      for k in xrange(j+1,len(trees)):
        if ( (trees[i][0] + trees[j][0] + trees[k][0]) % 3 , (trees[i][1] + trees[j][1] + trees[k][1]) % 3 ) == (0,0):
          result += 1
  
  # string.join(map(str,result))
  sys.stdout.write("Case #%s: %s\n" % (case + 1, result) )