#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint

def solve(s):
  t = int(s.readline())

  for i in range(t):
    r = int(s.readline()) - 1
    for i in range(4):
      texts = s.readline()
      if i == r:
        rows1 = set([int(i) for i in texts.split()])

    r = int(s.readline()) - 1
    for i in range(4):
      texts = s.readline()
      if i == r:
        result = rows1.intersection([int(i) for i in texts.split()])
    
    if len(result) > 1:
      yield 'Bad magician!'
    if len(result) == 0:
      yield 'Volunteer cheated!'
    if len(result) == 1:
      yield str(result.pop())  
    

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
