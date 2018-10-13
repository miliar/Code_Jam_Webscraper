#!/usr/bin/env python
import itertools
def solve(a):
	ans=0
	while a:
		x=min(a)
		i=a.index(x)
		del a[i]
		ans+=min(i,len(a)-i)
	return ans
for t in xrange(1,1+int(raw_input())):
	n=int(raw_input())
	a=map(int,raw_input().split())
	ans=solve(a)
	print"Case #%d:"%t,
	print ans
