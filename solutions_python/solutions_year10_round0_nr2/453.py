#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 2.5.2
 
import sys

def gcd(m, n):
	while(n != 0):
		r = m % n
		m = n
		n = r
	return m

def gcds(l):
	tmp = l[0]
	for i in range(1,len(l)):
		tmp = gcd(tmp, l[i])
	return tmp


if __name__=='__main__':
	C = int(sys.stdin.readline())

	for i in range(0,C):
		s = sys.stdin.readline().split()
		ts = [int(k) for k in s][1:]
		ts.sort()
		delta = [abs(ts[k] - ts[k-1]) for k in range(0,len(ts))][1:]
		cfact = gcds(delta)
		
		if ts[0]%cfact == 0:
			print "Case #%d: 0"%(i+1)
		else:
			print "Case #%d: %d"%(i+1, cfact - ts[len(ts)-1]%cfact)
	
