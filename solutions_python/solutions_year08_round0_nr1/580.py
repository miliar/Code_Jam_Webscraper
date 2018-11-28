#!/bin/env python 
# -*- coding: iso-8859-1 -*-
import os
import sys
import re

def func(se, queries):
  """
  >>> func(['Yeehaw','NSM','Dont Ask','B9','Googol'], ['Yeehaw','Yeehaw','Googol','B9','Googol','NSM','B9','NSM','Dont Ask','Googol'])
  '1'
  
  >>> func(['Yeehaw','NSM','Dont Ask','B9','Googol'], ['Googol', 'Dont Ask', 'NSM', 'NSM', 'Yeehaw', 'Yeehaw', 'Googol'])
  '0'

  """

  switches = 0
  
  s = se[:]
  ultimo = None
  for i in queries:
    try:
      if len(s)==1:
        ultimo = s[0]

      s.remove(i)
    except ValueError:
      pass

    if len(s)==0:
      switches += 1
      s = se[:]
      if ultimo is not None:
        s.remove(ultimo)
        ultimo = None

  return str(switches)

def main():
  #f = open('A-small.in')
  f = open('A-large.in')
  casos = int(f.readline())
  for testes in range(casos):
    se = []
    for i in range(int(f.readline())):
      se.append(f.readline().strip())
    q = []
    for i in range(int(f.readline())):
      q.append(f.readline().strip())
    print 'Case #%s: %s' % (testes+1, func(se, q))
  
  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
