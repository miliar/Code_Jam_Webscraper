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
  P,K,L = map(int,sys.stdin.readline().strip().split())
  
  letters = map(int,sys.stdin.readline().strip().split())
  
  letters.sort(reverse=True)
  
  if L > P * K:
    sys.stdout.write("Case #%s: Impossible\n" % case + 1)
  else:
    result = 0
    for i,num in enumerate(letters):
      result += (int(i/K) + 1) * num
    sys.stdout.write("Case #%s: %s\n" % (case + 1, result))
  # string.join(map(str,result))