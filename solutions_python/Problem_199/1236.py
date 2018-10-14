#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10000)

def flip(s, K, count):
  s2 = s.strip('+')
  if s2 == '':
    return count
  if len(s2) < K:
    return 'IMPOSSIBLE'
  s3 = ''
  for k in xrange(0, K):
    if s2[k] == '+':
      s3 += '-'
    if s2[k] == '-':
      s3 += '+'
  s3 += s2[K:]
  return flip(s3, K, count+1)


def solve(t, i):
  S, K = t[i].split(' ')
  K = int(K)
  print 'Case #%d: %s'%(i+1, flip(S, K, 0))

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t, k)
