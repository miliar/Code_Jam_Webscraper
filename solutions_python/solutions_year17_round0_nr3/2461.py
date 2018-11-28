#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def solve(n, k):
  intervals = [(0, n + 1)]
  for p in xrange(k):
      max_ii = -1
      max_ls = -1
      max_rs = -1
      max_s = -1
      for ii in xrange(len(intervals)):
          interval = intervals[ii]
          if interval[1] - interval[0] <= 1:
              continue
          middle = interval[0] + ((interval[1] - interval[0]) / 2)
          ls = middle - interval[0] - 1
          rs = interval[1] - middle - 1
          if ls > max_ls or rs > max_rs:
              max_ii = ii
              max_ls = ls
              max_rs = rs
              max_s = middle
      interval = intervals.pop(max_ii)
      intervals.append((interval[0], max_s))
      intervals.append((max_s, interval[1]))
  return [max(max_ls, max_rs), min(max_ls, max_rs)]

def main():
  cases = int(sys.stdin.readline().strip())
  for case in xrange(cases):
    s = solve(*map(int, sys.stdin.readline().strip().split()))
    print 'Case #%d: %d %d' % (case + 1, s[0], s[1])
  return 0

if __name__ == '__main__':
  #import pdb; pdb.set_trace()
  #print solve(4, 2)
  #sys.exit(0)
  sys.exit(main())
