#!/usr/bin/python

T=int(raw_input())

for case in xrange(T):
  [N,K]=map(int,raw_input().split())

  if K%(2**N)==(2**N-1): 
	s='ON'
  else:
	s='OFF'

#  print N, K,
  print 'Case #%d: %s'%(case+1, s)

