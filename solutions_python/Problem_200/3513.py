#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def solve(n):
  l = len(n)
  if l == 1:
    return int(n)
  n = map(int, n)
  i = l - 2
  while i > -1:
    a, b = n[i], n[i + 1]
    if a > b:
      if i > 1:
        n = n[:i - 1]
      elif i == 1:
        n = [n[0]]
      else:
        n = []
      n += [a - 1]
      n += [9] * (l - i - 1)
    i -= 1
  n = map(str, n)
  return int(''.join(n))

def main():
  cases = int(sys.stdin.readline().strip())
  for case in xrange(cases):
    print 'Case #%d: %d' % (case + 1, solve(sys.stdin.readline().strip()))
  return 0

if __name__ == '__main__':
  sys.exit(main())
