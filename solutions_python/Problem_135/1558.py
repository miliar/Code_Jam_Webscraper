#!/usr/bin/env python

import sys

def read_grid(f):
  arr = []
  for i in xrange(4):
    arr.append(f.readline().strip().split())
  return arr

case_num = 1
def solve(first_ans, first_grid, second_ans, second_grid):
  global case_num
  intersect = set(first_grid[first_ans-1]) & set(second_grid[second_ans-1])
  if (len(intersect)) == 1:
    output = int(intersect.pop())
  elif (len(intersect)) == 0:
    output = "Volunteer cheated!"
  else:
    output = "Bad magician!"
  print "Case #%d: %s" % (case_num, output)
  case_num += 1

with open(sys.argv[1],'r') as f:
  num_testcases = int(f.readline())
  for i in xrange(num_testcases):
    first_ans = int(f.readline())
    first_grid = read_grid(f)
    second_ans = int(f.readline())
    second_grid = read_grid(f)
    solve(first_ans, first_grid, second_ans, second_grid)
