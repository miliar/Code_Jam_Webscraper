#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint

def solveD(naomi, ken):
  l = len(naomi)
  ki = 0
  d = l
  for n in naomi:
    if n > ken[ki]:
      ki += 1
    else:
      d -= 1

    if ki == d:
      break

  return d

def solveW(naomi, ken):
  l = len(naomi)
  ki = 0
  w = l
  for n in naomi:
    while (ki < l) and (n > ken[ki]):
      ki += 1
    if ki == l:
      break
    ki += 1
    w -= 1
    if ki == l:
      break
  return w


def solveCase(naomi, ken):
  naomi.sort()
  ken.sort()

  print(naomi)
  print(ken)

  
  w = solveW(naomi, ken)
  d = solveD(naomi, ken)

  return d, w

def solve(s):
  t = int(s.readline())

  for i in range(t):
    n = int(s.readline())
    naomi = [round(float(f) * 100000) for f in s.readline().split()]
    ken = [round(float(f) * 100000) for f in s.readline().split()]
    print('Case ' + str(i + 1))
    d, w = solveCase(naomi, ken)
    print(d,w)
    yield str(d) + ' ' + str(w)

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': ' + case + '\n')
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)
