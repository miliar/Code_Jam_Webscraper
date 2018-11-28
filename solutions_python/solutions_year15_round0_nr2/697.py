#!/usr/bin/python

import sys

M = {}

def eat(s):
  s = ''.join(sorted(s))
  try:
    return M[s]
  except KeyError:
    pass
  ld = ord(s[-1]) - ord('0')
  best = ld
  for i in xrange(1, ld):
    x1 = ld - i
    ns = s[:-1] + '%s%s' % (chr(i + ord('0')), chr(ld - i + ord('0')))
    best = min(best, 1 + eat(ns))
  M[s] = best
  return best


T = int(sys.stdin.readline().strip())
for t in xrange(1, T + 1):
  D = int(sys.stdin.readline().strip())
  plates = ''.join(sys.stdin.readline().split())
  M.clear()
  print 'Case #%d: %d' % (t, eat(plates))
