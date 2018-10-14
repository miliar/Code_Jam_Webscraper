# -*- coding: utf-8 -*-
from math import *

fin = open("A-large.in")
fout = open("A-large.out","w")

cases= int(fin.readline().split()[0])
case = 0

def answer(x):
	global case, cases
	case += 1
	print >>fout, "Case #"+str(case)+": "+str(x)
	print "Case #"+str(case)+": "+str(x)
	
for test in xrange(cases):
	n,pd,pg = map(int, fin.readline().split())
	m = n
	f=1
	if (pg==100 and pd!=100):
		answer("Broken")
		continue
	if (pg==0 and pd==0):
		answer("Possible")
		continue
	if (pg==0 and pd!=0):
		answer("Broken")
		continue
	if n<100:
		for i in xrange(n+1):
			k= (i*pd)/100
			print k,i
			if (not k): continue
			if k*100==i*pd:
				answer("Possible")
				f=0
				break
		if (f):
			answer("Broken")
	else:
		answer("Possible")
	
