#!/usr/bin/env python
from fractions import gcd
from sys import stdin
T=int(stdin.readline())
for case in range(1, T+1):
	N, Pd, Pg=map(int, stdin.readline().split())
	d=100/gcd(100, Pd)
	if d>N or Pg==100 and Pd<100 or Pg==0 and Pd>0:
		p="Broken"
	else:
		p="Possible"
	print "Case #%d:"%case, p

