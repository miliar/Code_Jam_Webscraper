#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint

def factor2(n):
  while (n % 2) == 0:
    n = n // 2
  return n

def solveCase(p, q):
  f = factor2(q)
  if (p % f) != 0:
    return 'impossible'

  g = 0
  while True:
    if p >= q:
      return g
    g += 1
    p *= 2
  return 1

def solve(s):
  t = int(s.readline())

  for i in range(t):
    p, q = [int(i) for i in s.readline().split('/')]
    print('Case ' + str(i + 1))
    r = solveCase(p, q)
    yield str(r)

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
