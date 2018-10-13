#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def solve(s, k):
    flips = 0
    while 1:
        while len(s) > 0 and s[0] == 1:
            s = s[1:]
        if len(s) < k:
            break
        flips += 1
        for i in xrange(k):
            s[i] ^= 1
    if s.count(0) > 0:
        return 'IMPOSSIBLE'
    else:
        return str(flips)

def main():
  cases = int(sys.stdin.readline().strip())
  for case in xrange(cases):
    line = sys.stdin.readline().strip().split()
    line[0] = line[0].replace('+', '1').replace('-', '0')
    line[0] = map(int, line[0])
    line[1] = int(line[1])
    print 'Case #%d: %s' % (case + 1, solve(line[0], line[1]))
  return 0

if __name__ == '__main__':
  sys.exit(main())
