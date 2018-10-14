#!/usr/bin/env python

import sys

case_num = 1

def cost(C, F, X, num_farms):
  cur_rate = 2
  cost = 0
  while num_farms > 0:
    num_farms -= 1
    cost += C / cur_rate
    cur_rate += F
  return (cost + X / cur_rate)

def solve(C, F, X):
  global case_num
  num_farms = 0
  best = cost(C, F, X, num_farms)
  while True:
    num_farms += 1
    c = cost(C, F, X, num_farms)
    if c < best:
      best = c
    else:
      break
  print "Case #%d: %.7f" % (case_num, best)
  case_num += 1

with open(sys.argv[1],'r') as f:
  num_testcases = int(f.readline())
  for i in xrange(num_testcases):
    C, F, X = map(float, f.readline().strip().split())
    solve(C, F, X)

