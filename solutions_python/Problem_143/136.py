#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint

def solveCase(a, b, k):
  print(a, b, k)
  r = 0
  for i in range(a):
    for j in range(b):
      c = i & j
      if c < k:
        r += 1

  return r

def solve(s):
  t = int(s.readline())

  for i in range(t):
    a, b, k = [int(i) for i in s.readline().split()]
    print('Case ' + str(i + 1))
    r = solveCase(a, b, k)
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
