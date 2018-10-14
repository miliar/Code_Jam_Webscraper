#!/usr/bin/python

import sys

f = open("in2.txt","rb")
t = int(f.readline())

for i in range(t):
	m = f.readline().split()
	n,s,p = int(m.pop(0)),int(m.pop(0)),int(m.pop(0))
	s1,s2 = 0,0
	for j in range(n):
		tt = int(m.pop(0))
		if (tt==0):
			if (p==0):
				s1+=1
		elif (tt==1):
			if (p<=1):
				s1+=1
		else:
			if (tt>=3*p-2):
				s1+=1
			elif (tt >= 3*p-4):
				s2+=1
	print "Case #{0:0d}:".format(i+1),s1+min(s2,s)
