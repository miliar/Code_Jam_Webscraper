#!/usr/bin/env python

import sys

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  A,B,K = [int(x) for x in rl().split()]
  ret = 0
  for i in xrange(A):
    for j in xrange(B):
      if i&j<K:
        ret += 1
  return ret

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
