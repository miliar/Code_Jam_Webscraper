#!/bin/env python 
# -*- coding: iso-8859-1 -*-
import os
import sys
import re
import string


def cai(m, i, j, x, y):
  v = m[j][i]
  r = None
  if j != 0 and m[j-1][i] < v:
    r = (j-1,i)
    v = m[j-1][i]
  if i != 0 and m[j][i-1] < v:
    r = (j,i-1)
    v = m[j][i-1]
  if i != x-1 and m[j][i+1] < v:
    r = (j, i+1)
    v = m[j][i+1]
  if j != y-1 and m[j+1][i] < v:
    r = (j+1, i)
     
  return r

def getAll(l, s):
  g = l[s].copy()
  for i in g:
    if i in l:
      getAll(l, i)
      l[s].update(l[i])
      del l[i]
  
def setGroup(m, l, i, j, letter):
  kj = ki = None
  if (j,i) in l:
    kj, ki = (j,i)
  else:
    for k, v in l.items():
      if (j,i) in v:
        kj, ki = k
        break
  if kj is None:
    import pdb;pdb.set_trace()
  m[kj][ki] = letter
  for lj,li in l[(kj,ki)]:
    m[lj][li]=letter
    
def func(m, x, y):
  l = {}
  sinks = []
  for j in range(y):
    for i in range(x):
      s = cai(m, i, j, x, y)
      if s is None:
        sinks.append((j,i))
      else:
        l.setdefault(s,set()).add((j,i))

  for s in sinks:
    if s in l:
      getAll(l, s)
    else:
      l[s] = set()


  ts = type('')
  letter = 0
  for j in range(y):
    for i in range(x):
      if type(m[j][i]) is not ts:
        setGroup(m, l, i, j, string.lowercase[letter])
        letter += 1
  return m

def main():
  #f = open('sample.in')
  #f = open('B-small-attempt0.in')
  f = open('B-large.in')
  t = int(f.readline())
  
  for i in range(t):
    y, x = f.readline().split()
    x = int(x)
    y = int(y)
    m = []
    for j in range(y):
      m.append([int(z) for z in f.readline().split()])
    print 'Case #%i:' % (i+1)
    for a in func(m, x, y):
      for b in a:
        print b,
      print
  
  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
