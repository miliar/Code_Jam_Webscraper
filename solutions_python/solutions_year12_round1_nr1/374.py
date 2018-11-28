#!/usr/bin/python

import sys

f = open("in1.txt","rb")
t = int(f.readline())

for i in range(t):
	m = map(int,f.readline().split())
	a,b = m[0],m[1]
	m = map(float,f.readline().split())
	def per(i):
		p = 1
		for ii in range(a-i):
			p*=m[ii]
		if (i>0 and i<=a):
			p*=(1-m[a-i])
		return p

	psum = 0
	k = b-a+1
	minex = b+2
	for j in range(min(a,(a+3)/2)):
		psum += per(j)
		newex = k*psum + (k+b+1)*(1-psum)
		if (newex < minex):
			minex = newex
		k+=2
	print("Case #{0:0d}: %.6f" % minex).format(i+1)
