#!/usr/bin/python

import sys
import math

test_cases = None
current_case = 0

precalculated = []

def solve(test_case, game):
  num = 0
  for n in precalculated:
    if n >= game[0] and n <= game[1]:
      num+=1

  print "Case #%d: %d" % (test_case, num)

def is_palindrome(s):
  return s == s[::-1]

def precalculate_range(minimum, maximum):
  smallest = int(math.floor(math.sqrt(minimum)))
  largest = int(math.ceil(math.sqrt(maximum)))
  for x in range(smallest, largest+1):
    sq = int(math.pow(x,2))
    if is_palindrome(str(x)) and is_palindrome(str(sq)):
      precalculated.append(sq)

precalculate_range(0,1001)

for line in sys.stdin:
  if not test_cases:
    test_cases = int(line)
  elif len(line.strip()) != 0:
    current_case+=1
    solve(current_case, [int(x) for x in line.strip().split(' ')])
  
