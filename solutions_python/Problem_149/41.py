#!/usr/bin/env python

for t in xrange(int(raw_input())):
  n = int(raw_input())
  A = map(int,raw_input().split())
  c = 0
  while A:
    m = min(A)
    k = min(i for i in xrange(len(A)) if A[i]==m)
    c += min(k, len(A)-k-1)
    del A[k]
  print 'Case #%d: %d' % (t+1, c)
