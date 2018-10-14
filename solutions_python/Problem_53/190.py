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
def n2b(n):
  result = ''
  while 1:
    n, d = divmod(n, 2)
    result = str(d) + result
    if n==0: return result

def solve():
  N, K = map(int, next(fin).split())
  state = n2b(K)
  state = '0' * N + state
  state = state[-N:]
  result = 'ON' if all(c=='1' for c in state) else 'OFF'
  
  print>>fout, result

#####################################################

cases = int(next(fin))
start = time.clock()
for case in xrange(cases):  
  print>>sys.stderr, '{0:5}/{1:<5}'.format( case, cases), '\b' * 13,
  print>>fout, 'Case #{0}:'.format( 1+case ),
  solve()

print>>sys.stderr, "[done in: {0:.3f} s]".format(time.clock()-start),

