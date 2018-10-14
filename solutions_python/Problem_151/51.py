#!/usr/bin/env python

from collections import defaultdict
from itertools import product

def cnt(T):
  if not T: raise Exception
  T = sorted(T)
  c = len(T[0])+1
  for i in xrange(1,len(T)):
    for j in xrange(0,len(T[i])):
      if len(T[i-1]) == j or T[i][j] != T[i-1][j]:
        c += len(T[i]) - j
        break
  return c

for t in xrange(int(raw_input())):
  m,n = map(int,raw_input().split())
  S = []
  for i in xrange(m):
    S.append(raw_input().strip())
  C = defaultdict(int)
  for ass in product(xrange(n), repeat=m):
    Ts = [list() for i in xrange(n)]
    for i in xrange(m):
      Ts[ass[i]].append(S[i])
    skip=False
    for i in xrange(n):
      if not Ts[i]:
        skip=True
        break
    if skip:continue
    c = sum(cnt(T) for T in Ts)
    C[c] += 1
  print 'Case #%d: %d %d' % (t+1, max(C), C[max(C)]%(10**9+7))
