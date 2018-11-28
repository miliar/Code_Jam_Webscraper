#!/usr/bin/env python

import sys

if __name__ == '__main__':
  N = int(sys.stdin.readline().strip())
  for i in xrange(N):
    S = int(sys.stdin.readline().strip())
    all = set()
    len_all = 0
    for j in xrange(S):
      all.add(sys.stdin.readline()[:-1])
      len_all += 1
    Q = int(sys.stdin.readline().strip())
    seen = 0
    seen_set = set()
    changes = 0
    for j in xrange(Q):
      next = sys.stdin.readline()[:-1]
      if next not in seen_set:
        seen += 1
        seen_set.add(next)
      if seen == len_all:
        seen_set = set()
        seen_set.add(next)
        seen = 1
        changes += 1
    print 'Case #%d: %d' % (i + 1, changes)
