#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Suryakumar Sudar <surya@k43sa-ubuntu>
  

import sys


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
	a=[]
	b=[]
	mat=[]
	no_test_cases=int(lines[0][0])
	lines=lines[1:]
	#print no_test_cases	
	for i in range(len(lines)):
		#print lines[i],"\n"
		if((i%10)==0 and i!=0):
			b.append(mat)
			mat=[]
			a.append(b)
			b=[]
			b.append(lines[i])
			#print lines[i]
		elif((i%5)==0 and i!=0):
			b.append(mat)
			b.append(lines[i])
			mat=[]
		elif i==0:
			b.append(lines[i])
		else:
			mat.append(lines[i])
	b.append(mat)
	a.append(b)
	
	return a		
	
def solve(a):
	for i in range(len(a)):
		e1=(a[i][0][0])
		m1=a[i][1]
		e2=(a[i][2][0])
		m2=a[i][3]
		
		#print e1,"\n", m1[e1-1],"\n"
		#print e2,"\n", m2[e2-1],"\n"
		
		flag_num=0
		
		
		
		for temp in m1[int(e1)-1]:
			if temp in m2[int(e2)-1]:
				common=str(temp)
				flag_num=flag_num+1
				
				
		#print flag_num
		
		if flag_num==1:
			print "Case #"+str(i+1)+": "+common
		elif flag_num==0:
			print "Case #"+str(i+1)+": Volunteer cheated!"
		else:
			print "Case #"+str(i+1)+": Bad magician!"
			
					
		
		
			
		
					

def main():
	lines = read(sys.argv[1])
	#print lines
	final_set=order(lines)

	solve(final_set)
	
	return 0

if __name__ == '__main__':
	main()

