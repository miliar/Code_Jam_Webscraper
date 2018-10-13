#!/usr/bin/env python
import sys

def findTotalCutoff(p):
  def c(s): return min(10, max(0, s))
  return (c(p) + c(p-2) + c(p-2), c(p) + 2 * c(p-1))

def getNumReachingTarget(N, S, p, t):
  x = findTotalCutoff(p)
  i = len([y for y in t if y >= x[0] and y < x[1]])
  j = len([y for y in t if y >= x[1]])
  return min(i, S) + j

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  for i in range(T):
    line = [int(x) for x in sys.stdin.readline().strip().split()]
    N, S, p, t = line[0], line[1], line[2], line[3:]
    print('Case #%d: %d' % (i + 1, getNumReachingTarget(N, S, p, t)))

