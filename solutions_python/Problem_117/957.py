#!/usr/bin/env python

import sys
import math

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  N,M = [int(x) for x in rl().split()]
  data = []
  for i in xrange(N):
    data.append([int(x) for x in rl().split()])
  ms = [0] * (N+M)
  for i in xrange(N):
    for j in xrange(M):
      ms[i] = max(ms[i],data[i][j])
  for i in xrange(M):
    s = set()
    for j in xrange(N):
      ms[N+i] = max(ms[N+i],data[j][i])
  d2 = []
  for i in xrange(N):
    d2.append([100]*M)
  for i in xrange(N):
    for j in xrange(M):
      d2[i][j] = min(d2[i][j],ms[i])
  for i in xrange(M):
    for j in xrange(N):
      d2[j][i] = min(d2[j][i],ms[i+N])
  for i in xrange(N):
    for j in xrange(M):
      if data[i][j] != d2[i][j]:
        return 'NO'
  return 'YES'

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
