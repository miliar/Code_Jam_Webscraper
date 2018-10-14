#!/bin/python2

import sys

def read_line():
  return sys.stdin.readline()

def read_int():
  return int(read_line())

def read_float():
  return float(read_line())

def solve(c, f, x):
  v = 2
  next_farm = c/v
  total = x/v
  while total > x/(v+f) + next_farm:
    v += f
    total = x/v + next_farm
    next_farm += c/v
  return total

T = read_int()
for i in xrange(1, T+1):
  c,f,x = map(float, read_line().split())
  sec = solve(c,f,x)
  print ("Case #%i: %.7f") % (i, sec)
