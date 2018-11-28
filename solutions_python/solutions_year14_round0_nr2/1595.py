#!/usr/bin/env python

import sys

def main():
  _f = sys.stdin
  caseCount = int(_f.readline().strip())
  for i in xrange(1, caseCount+1):
    c, f, x = getInput(_f)
    duration = solve(c, f, x)
    displayAndClear(i, duration)

def getInput(_f):
  c, f, x = [float(arg) for arg in _f.readline().split()]
  return c, f, x

def displayAndClear(i, duration):
  print 'Case #%d: %.7f' % (i, duration)

def solve(c, f, x):
  duration = 0.0
  rate = 2.0 # initial rate
  while True:
    noFarm = x / rate
    improve = c / rate
    farm = improve  + x/(rate + f)
    if farm < noFarm:
      duration += improve
      rate += f
    else:
      duration += noFarm
      break

  return duration

if __name__ == '__main__':
  main()

