#coding: 1251
#####################################################

from __future__ import division

import os
import sys
import operator
import string
import re
import time


from os.path import splitext
from copy import copy

from math import *
from collections import *
from itertools import *
from functools import *

if len(sys.argv)<=1: 
  sys.argv += [ re.match(r'.*(\w)\w*\.py.*', sys.argv[0]).group(1) + '-tiny.in' ]  

fin, fout = open(sys.argv[1], 'r'), open(splitext(sys.argv[1])[0]+'.out', 'w+')

#####################################################

def gcd(a, b):
  while a != b:
    if a>b: 
      c = a - b
      c = b * (c // b)
      if c: a -= c
      else: a -= b
    else: 
      c = b - a
      c = a * (c // a)
      if c: b -= c
      else: b -= a      

  return a

def solve():
  nums = map(int, next(fin).split())
  assert len(nums) == nums[0] + 1
  del nums[0]

  nums = sorted(set(nums))
  first = min(nums)
  del nums[0]
  nums = [k-first for k in nums]

  d = reduce(gcd, nums)

  if first % d == 0: result = 0
  else:
    result = d - first % d
  
  print>>fout, result

#####################################################

cases = int(next(fin))
start = time.clock()
for case in xrange(cases):  
  print>>sys.stderr, '{0:5}/{1:<5}'.format( case, cases), '\b' * 13,
  print>>fout, 'Case #{0}:'.format( 1+case ),
  solve()

print>>sys.stderr, "[done in: {0:.3f} s]".format(time.clock()-start),

