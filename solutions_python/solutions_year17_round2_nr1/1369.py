#!/usr/bin/python

from sys import *

n_cases = int(stdin.readline().rstrip("\n"),10)

for case in range(0,n_cases):
	result=0
	line=stdin.readline().rstrip("\n").split()
	distance=int(line[0],10)
	number_of_h=int(line[1],10)
	hs={}
	for i in range(0,number_of_h):
		line_h=stdin.readline().rstrip("\n").split()
		hs[int(line_h[0],10)]=int(line_h[1],10)

	keys = sorted(hs.keys())
	hours = (distance-keys[0]*1.0)/hs[keys[0]]*1.0
	result = distance*1.0/hours
	for j in range(1,len(keys)):
		hours_h= (distance-keys[j]*1.0)/hs[keys[j]]*1.0
		if hours<hours_h:
			 hours = (distance-keys[j]*1.0)/hs[keys[j]]*1.0
		         result = distance*1.0/hours

	print("Case #"+str(case+1)+": "+"%0.6f"%result)

