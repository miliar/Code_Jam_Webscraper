#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 S uryakumar Sudar <surya@k43sa-ubuntu>
  

import sys
import decimal


def read(filename):
	f=open(filename,'r')
	lines=f.readlines()
	newlines=[]
	words=[]
	for i in lines:
		words=i.split(" ")	
		words[-1]=words[-1][:-1]
		#print words	
		newlines.append(words)
	return newlines	

def order(lines):
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			lines[i][j]=float(lines[i][j])
	
	#print lines
	return lines
	
def hamlet(rate,C,F,X):
	if ( X/rate < C/rate + X/(rate+F) ):
		return 0
	else:
		return 1
	
def solve(rate,time,C,F,X):
	while(hamlet(rate,C,F,X) == 1):
		time=time+C/rate
		rate=rate+F
	time=time+X/rate
	#print time
	final_ans = decimal.Decimal(time)
	final_ans = round(final_ans,7)
	return final_ans
	
		
def solve_major(a):
	for i in range(len(a)):
		C=a[i][0]
		F=a[i][1]
		X=a[i][2]
		
		rate=2
		time=0.0
		flag=1
		
		a2=solve(rate,time,C,F,X)
		#print a2
		print "Case #"+str(i+1)+": "+str(a2) 
		
	
def main():
	lines = read(sys.argv[1])
	no_test_cases=int(lines[0][0])
	lines=lines[1:]
	final_set=order(lines) 
	solve_major(final_set)
	#print no_test_cases
	#print lines
	
	return 0

if __name__ == '__main__':
	main()

