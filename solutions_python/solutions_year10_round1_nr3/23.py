from __future__ import with_statement
from math import pow
from collections import defaultdict
from pprint import pprint as pp

import pickle
import pdb
import sys
import os
import math

from numpy import *

def parseIntLine(line):
  return [int(x) for x in line[:-1].split(" ")]

def main():
  with open(sys.argv[1],'r') as f:
    with open('test.out','w') as g:
      cases = int(f.readline()[:-1]) # number cases
      for j,line in enumerate(f):
        case = parseIntLine(line)
        ans = computeAnswer(*case)
        g.write("Case #%d: %d\n" % (j+1,ans))


def computeAnswer(a1,a2,b1,b2):
  wins = 0
  for a in range(a1,a2+1):
    for b in range(b1, b2+1):
      if isWin(a,b):
        wins += 1
  return wins

def isWin(a,b):
  # WLOG
  if b > a:
    a,b = b,a

#   print a,b
  if a == b:
    return False
  c = a % b
  if c == 0:
    return True

  if a > 2*b:
    return not isWin(b,c) or not isWin(b+c,b)
  else:
    return not isWin(a-b,b)

#   test = c
#   found = False
#   while test > 0:
#     if not isWin(test,b):
#       return True
#     test += b
#   return False





if __name__=="__main__":
  main()
