#!/usr/bin/env python
from sys import stdin
T=int(stdin.readline())
for case in range(1, T+1):
	N=int(stdin.readline())
	C=map(int, stdin.readline().split())
	B=map(bin, C)
	for p in range(-20, 0):
		c=0
		for b in B:
			if len(b)<2-p:continue
			if b[p]=='1':c+=1
		if c%2:
			C="NO"
			break
	else:
		C=sum(C)-min(C)
	print "Case #%d:"%case, C

