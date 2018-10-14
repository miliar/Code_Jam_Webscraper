#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(m, s):
  r = 0
  standing = 0
  for needed in range(0, m + 1):
    if needed > standing:
      r = r + (needed - standing)
      standing = needed

    standing = standing + int(s[needed])
  return r

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    m, l = s.readline().split()
    yield solveCase(int(m), l)

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