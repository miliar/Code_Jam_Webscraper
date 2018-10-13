#!/usr/bin/env python
# encoding: utf-8
"""
CODEJAM TEMPLATE

Created by Jamie Smith


"""

import sys
import os
	
def readints(f):
	return map(int, f.readline().split())

def digits(n):
	result=[]
	b=1
	while n>0:
		result.append(n%(10*b)/b)
		n-=n%(10*b)
		b=b*10
	result.reverse()
	return result
		
def cycle(l):
	return [l[-1]]+l[0:-1]
	
def allcycles(l):
	res=[l]
	for i in range(len(l)-1):
		res.append(cycle(res[-1]))
	res.sort()
	return res

def choose2(n):
	return n*(n-1)/2
	
def unique(L):
	result={}
	for l in L:
		result[l]=0
	return result.keys()

def main():
	os.chdir("/Users/Jamie/Documents/Codejam")
	
	# f=open('input.txt','r')
	f=open('C-small-attempt0.in','r')
	# f=open('A-large-practice.in','r')
	o=open('recyclingout.txt','w')
	
	T=int(f.readline())



	for j in range(T):
		A,B=readints(f)
		R=map(digits,range(A,B+1))
		R=map(allcycles,R)
		R=map(str,R)
		U=unique(R)
		result=0
		for u in U:
			result+=choose2(R.count(u))
		
		# print "Case #%s: %s\n" % (j+1,result)
		o.write("Case #%s: %s\n" % (j+1,result))
	f.close()
	o.close()

if __name__ == '__main__':
	main()


