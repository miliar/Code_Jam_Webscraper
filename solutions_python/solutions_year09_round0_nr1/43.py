#!/bin/env python 
# -*- coding: iso-8859-1 -*-
import os
import sys
import re

def func(theinput):
  """
  >>> func('')
  ''
  
  >>> func('')
  ''
  
  >>> func('')
  ''
  
  >>> func('')
  ''
  """
  num, digFrom, digTo = theinput.split()

  return ''

def montaRe(t):
  r = []
  gr = False;
  g = []
  for i in t:
    if i == '(':
      gr = True
    elif i == ')':
      gr = False
      r.append('(?:' + '|'.join(g) + ')')
      g = []
    else:
      if gr:
        g.append(i)
      else:
        r.append(i)
  return re.compile(''.join(r))

def func(w, pat):
  t = 0
  for i in w:
    if pat.match(i):
      t += 1
  return t
  
def main():
  #f = open('A-test.in')
  #f = open('A-small-attempt0.in')
  f = open('A-large.in')
  l,d,n = [int(i) for i in f.readline().split()]
  w = []
  for i in range(d):
    w.append(f.readline().strip())

  for i in range(n):
    print 'Case #%s: %s' % (i+1, func(w, montaRe(f.readline().strip())))

  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
