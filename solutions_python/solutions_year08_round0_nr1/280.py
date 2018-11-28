#!/usr/bin/env python
# encoding: utf-8
"""
problemA.py

Created by Jesse Krijthe on 2008-07-17.
"""

import sys
import os

def count(se, qs):
	currentfind=[0,0]
	for e in se:
		try:
			if qs.index(e)>currentfind[1]:
				currentfind=[e, qs.index(e)]
		except:
			return [e, 'done']
	return currentfind

def agent(se, qs):
	if count(se, qs)[1]=='done':
		return 0
	else:
		switches=0
		while len(qs)!=0:
			c=count(se, qs)
			if c[1]=='done':
				break
			else:
				switches=switches+1
				qs=qs[c[1]:]
		return switches	
	
if __name__ == '__main__':
	fileHandle = open ('big.in')
	fileOut=open('output','w')
	N = int(fileHandle.readline())	
	for n in range(N):
		se=[]
		qs=[]
		for sl in range(int(fileHandle.readline())):
			se.append(fileHandle.readline())
		for ql in range(int(fileHandle.readline())):
			qs.append(fileHandle.readline())
		fileOut.write("Case #"+str(n+1)+": "+str(agent(se,qs))+"\n")
	fileHandle.close()
	fileOut.close()

