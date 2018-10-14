#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gcd(a,b):
	a,b=min(a,b),max(a,b)
	if a==0:
		return b
	return gcd(b%a,a)

c=input()
for i in xrange(1,c+1):
	f=[int(x) for x in raw_input().split()]
	n=f[0]
	f=f[1:]
	m=min(f)
	f=[x-m for x in f]
	t=f[0]
	for k in f[1:]:
		t=gcd(t,k)
	if m%t==0:
		x=0
	else:
		x=(m/t+1)*t-m
	print 'Case #%d: %d' %(i,x)