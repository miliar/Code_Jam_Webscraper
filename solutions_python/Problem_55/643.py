#!/usr/bin/env python 
# -*- coding: iso-8859-1 -*-

import bisect, sys

def func(numTurns, capacity, numGroups, g):
  subTotal = 0
  acum = []
  for i in g:
    subTotal += i
    acum.append(subTotal)

  euros = 0
  startPos = 0
  turn = 0
  while turn < numTurns:
    filled = 0
    simCap = capacity
    if startPos > 0:
      simCap += acum[startPos-1]
    pos = bisect.bisect_right(acum, simCap, startPos, numGroups)
    if pos > 0:
      filled = acum[pos-1]
      if startPos > 0:
        filled -= acum[startPos-1]

      if pos == numGroups:
        otherPos = bisect.bisect_right(acum, capacity - filled, 0, startPos)
        if otherPos > 0:
          filled += acum[otherPos-1]
        startPos = otherPos
      else:
        startPos = pos
    euros += filled
    turn += 1
  return euros
  
def main():
  #f = open('C-test.in')
  f = open('C-small-attempt0.in')
  #f = open('C-large.in')
  n = int(f.readline())
  
  for j in range(n):
    r, k, n = [int(i) for i in f.readline().split()]
    g = [int(i) for i in f.readline().split()]
    print 'Case #%s: %s' % (j+1, func(r, k, n, g))

  
def _test():
  import doctest
  doctest.testmod()


if __name__ == "__main__":
  if len(sys.argv) > 1:
    _test()
  else:
    main()
