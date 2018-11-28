#!/usr/bin/env python

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a%b)

C = int(raw_input())
for case in range(C):
  l = [long(s) for s in raw_input().split(' ')]
  N = l[0]
  l = l[1:]
  l.sort()
  l.reverse()
  diffs = [l[i] - l[j] for i in range(len(l)-1)
                       for j in range(i+1, len(l))]
  T = reduce(gcd, diffs)
  if l[0] % T == 0: print 'Case #%i: 0' % (case+1)
  else: print 'Case #%i: %i' % (case+1, T-(l[0]%T))
