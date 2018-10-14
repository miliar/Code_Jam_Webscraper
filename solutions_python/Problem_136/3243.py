#!/usr/bin/env python

import sys
import select

test_case = """4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
"""

sys.setrecursionlimit(10**3)

IS_INPUT = len(select.select([sys.stdin,],[],[],0.0)[0])
test_input = test_case.split("\n")

def miline():
  return map(int, get_line().split(" "))

def mfline():
  return map(float, get_line().split(" "))

def iline():
  return int(get_line())

def fline():
  return float(get_line())

def get_line():
  if IS_INPUT > 0:
    return sys.stdin.readline()
  return test_input.pop(0)

#------------------

def solve(C,F,X,CPS,time):

  # Find out next X on current CPS
  cur_best = float("inf")

  while True:
    ng_time = time + (X / CPS)
    # Find out next C build time on current CPS
    if ng_time > cur_best:
      break

    cur_best = ng_time

    time = time + (C / CPS)
    CPS = CPS + F

    nf_solve_time = time + (X / CPS)
    if cur_best < nf_solve_time:
      break

  return cur_best

num_cases = iline()
test_case = 1

while test_case < num_cases + 1:
  [C, F, X] = mfline()
  #try:
  shortest = solve(C, F, X, 2.0, 0.0)
  #except:
  #  print C, CPSF, X
  #  #import pdb; pdb.set_trace()
  
  print "Case #{}: {:.6f}".format(test_case, shortest)
  test_case += 1
