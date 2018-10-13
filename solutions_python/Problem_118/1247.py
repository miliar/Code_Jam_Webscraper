#!/usr/bin/env python

import sys
import math

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  def checkp(x):
    l = list(str(x))
    l.reverse()
    return int(''.join(l)) == x
  def check(x):
    if not checkp(x):
      return False
    y = int(math.sqrt(x))
    return y*y == x and checkp(y)
  A,B = [int(x) for x in rl().split()]
  c = 0
  for i in xrange(A,B+1):
    if check(i):
      c += 1
  return c

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
