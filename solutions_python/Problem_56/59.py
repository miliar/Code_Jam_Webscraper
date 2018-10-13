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


try:
    import psyco
    psyco.full()
except ImportError:
    print 'Psyco not installed, the program will just run slower'

#####################################################

def solve():
  N, K = map(int, fin.next().split())
  field = map(string.strip, islice(fin, N))

  assert all(len(f) == N for f in field)

  for ii, f in enumerate(field[:]):
    r = []
    for c in f:
      if c!='.': r += [c]
    r[0:0] = ['.'] * (N - len(r))
    field[ii] = ''.join(r)
  
  def neighbours(i,j):
    for ix, ii,jj in [[0,+1,0],[1,+1,+1],[2,0,+1],[3,-1,1]]:
      if 0 <= i+ii < N and 0 <= j+jj < N:
        yield (ix, i+ii,j+jj)

  find = {}
  for j in xrange(N-1,-1,-1):
    for i in xrange(N-1,-1,-1):
      find[i,j] = { 'R':{0:0, 1:0, 2:0, 3:0}, 'B':{0:0, 1:0, 2:0, 3:0} }

  maxim = {'R':0, 'B':0}
  for j in xrange(N-1,-1,-1):
    for i in xrange(N-1,-1,-1):
      c = field[i][j]
      if c != '.':
        for ix in find[i,j][c]:
          find[i,j][c][ix] = 1

        for ix, ii, jj in neighbours(i,j):
          prev = find[ii,jj][c][ix]
          find[i,j][c][ix] = prev+1
          maxim[c] = max(prev+1, maxim[c])

  R, B = maxim['R'] >= K, maxim['B'] >= K

  #print field
  #print maxim
  #print

  if R and B: return 'Both'
  elif R: return 'Red'
  elif B: return 'Blue'
  else: return 'Neither'

#####################################################

if len(sys.argv)<=1: 
  sys.argv += [ re.match(r'.*(\w)\w*\.py.*', sys.argv[0]).group(1) + '-tiny.in' ]  

fin, fout = open(sys.argv[1], 'r'), open(splitext(sys.argv[1])[0]+'.out', 'w+')

start = time.clock()
def working_on(case, cases):
  delt = (time.clock() - start)
  est = delt * cases / case if case else 0.0
  msg = 'now: %s/%s, %.0f/%.0fs' % (1+case, cases, delt, est)
  if case < cases: 
    return msg + '\b' * (len(msg)+1)
  else:
    return ' ' * (len(msg)+1) + '\b' * (len(msg)+1) + \
           "[done in: %.3f s]" % (time.clock()-start)

cases = int(fin.next())
for case in xrange(cases):  
  print>>sys.stderr, working_on(case, cases),
  print>>fout, 'Case #%d: %s' % ( 1+case, solve() )
  

print>>sys.stderr, working_on(0,0),


