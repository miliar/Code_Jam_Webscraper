#!/usr/bin/env python3
# encoding: utf-8

import sys
from pprint import pprint

def solveCase(ps):
  m = max(ps)
  result = 10000000
  for i in range(1, m + 1):
    minutes = i
    for p in ps:
      if p <= i:
        continue
      d, r = divmod(p, i)
      if r == 0:
        d -= 1

      minutes += d

    if minutes < result:
      result = minutes

  return result

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    d = int(s.readline())
    ps = [int(x) for x in s.readline().split()]
    yield solveCase(ps)

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