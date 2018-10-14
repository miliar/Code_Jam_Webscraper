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
  from do import report_working_on, filein, fileout
except ImportError:
  report_working_on = lambda a,b: None
  filein = lambda: sys.stdin
  fileout = lambda: sys.stdout

def dorun():
  fin, fout = filein(), fileout() 
  cases = int(fin.next())
  for case in xrange(cases):  
    report_working_on(case, cases)
    print>>fout, 'Case #%d: %s' % ( 1+case, solve(fin) )
  else:  
    report_working_on(0,0)

try:
    import psyco
    psyco.full()
except ImportError:
    print 'Psyco not installed, the program will just run slower'

#####################################################

class memoize(object):
  def __init__(self, f):
    self.f = f
    self.cache = {}
  def __call__(self, *args):
    k = tuple(args)
    v = self.cache.get(k, None)
    if v is None: 
      v = self.f(*args)
      self.cache[k] = v
    return v

#####################################################

def solve(fin):
  R = int(fin.next())

  toList = lambda s: map(int, s.split())
  XYXY = map(toList, islice(fin, R))

  area = {}
  for X1, Y1, X2, Y2 in XYXY:
    for x in xrange(X1,X2+1):
      for y in xrange(Y1,Y2+1):
        area[x,y] = 1

  for seconds in range(10000):
    if not area: break

    newarea = area.copy()
    for (x,y),_ in area.iteritems():
      if not area.get((x,y-1)) and not area.get((x-1,y)): #die
        del newarea[x,y]
      if area.get((x,y)) and area.get((x-1, y+1)): # born down
        newarea[x,y+1] = 1
    area = newarea

  return seconds

#####################################################

if __name__=='__main__': dorun()
