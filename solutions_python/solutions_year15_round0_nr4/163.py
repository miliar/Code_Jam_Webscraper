#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(x, r, c):
  if x == 1:
    return 'GABRIEL'

  if x > 6:
    return 'RICHARD'

  if ((x - 1) // 2 + 1) > min(r, c):
    return 'RICHARD'

  d, r = divmod(r * c, x)
  if r != 0:
    return 'RICHARD'

  if d < 2:
    if x > 2:
      return 'RICHARD'

  if d == 2:
    if x > 3:
      return 'RICHARD'

  return 'GABRIEL'

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    x, r, c = [int(x) for x in s.readline().split()]
    yield solveCase(x, r, c)

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': ' + str(case) + '\n')
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)