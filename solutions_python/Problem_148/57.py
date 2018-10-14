#!/usr/bin/env python

for t in xrange(int(raw_input())):
  n,x = map(int, raw_input().split())
  S = sorted(map(int,raw_input().split()))
  top = n
  for i in xrange(n):
    flag = False
    for j in xrange(top-1,i,-1):
      if S[i]+S[j] <= x:
        top = j
        flag = True
        break
    if not flag:
      break
  print 'Case #%d: %d' % (t+1, n-i)
