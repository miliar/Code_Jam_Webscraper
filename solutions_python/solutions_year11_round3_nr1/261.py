# -*- coding: utf-8 -*-
from math import *
import re

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
	r,c = map(int, fin.readline().split())
	t=[]
	res=""
	for i in xrange(r):
		t.append(fin.readline()[:-1])
	for i in xrange(r-1):
		for j in xrange(c-1):
			if (t[i][j]=="#"):
				if (t[i+1][j]=="#" and t[i][j+1]=="#" and t[i+1][j+1]=="#"):
					t[i]=t[i][:j]+"/\\"+t[i][j+2:]
					t[i+1]=t[i+1][:j]+"\\/"+t[i+1][j+2:]
	for i in xrange(r):
		if "#" in t[i]: res="\nImpossible\n"
	if (not res):
		res="\n"
		for i in xrange(r):
			res+=t[i]
			res+="\n"
	answer(res[:-1])	
	
	
	
	
	
	
	
	
	
	
	
	
	


