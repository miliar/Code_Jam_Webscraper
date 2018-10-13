#!/bin/env python 
# -*- coding: iso-8859-1 -*-
import os
import sys
from bisect import bisect_left as  bisect

s = "welcome to code jam"
m = {}
precalculo = {}

def func(l):
  letters = set(s)
  m.clear()
  precalculo.clear()
  for i in range(len(l)):
    if l[i] in letters:
      m.setdefault(l[i],[]).append(i)

  if s[0] not in m:
    return 0
  return count(0, m[s[0]][0])
    
def count(letter, pos):
  if s[letter] not in m:
    return 0
  a = m[s[letter]]
  achou = bisect(a, pos)
  l = len(a)
  if achou == l:
    return 0
  if letter == 18:
    return len(a) - achou

  #se tiver mais caracteres a achar do que tem string, é zero

  if (letter, achou) in precalculo:
    return precalculo[(letter, achou)]
  
  total = 0
  for i in range(achou, l):
    total += count(letter+1, a[i]+1)
    if total >= 10000:
      total %= 10000
  precalculo[(letter, achou)] = total
  return total
     
  

def main():
  #f = open('sample.in')
  #f = open('C-small-attempt0.in')
  f = open('C-large.in')
  c = int(f.readline())
  for i in range(c):
    l = f.readline().strip()
    print 'Case #%s: %04d' % (i+1, func(l))
  
  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
