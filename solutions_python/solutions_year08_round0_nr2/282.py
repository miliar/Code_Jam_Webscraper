#!/usr/bin/env python
# encoding: utf-8
"""
problemB.py

Created by Jesse Krijthe on 2008-07-17.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from string import *


def main(inputFile):
	turnaround=int(inputFile.readline())
	(tripsab, tripsba)=inputFile.readline().split(' ')
	
	a2bl=[] #a2b leaving times
	a2ba=[] #a2b arrival times
	b2al=[] #b2a leaving times
	b2aa=[] #b2a arrival times
	
	for l in range(int(tripsab)):
		(departure, arrival)=inputFile.readline().rstrip().split(' ')
		a2bl.append(departure)
		a2ba.append(arrival)
	for l in range(int(tripsba)):
		(departure, arrival)=inputFile.readline().rstrip().split(' ')
		b2al.append(departure)
		b2aa.append(arrival)
	
	#print a2bl, a2ba, b2al, b2aa
	
	tca=0 # trains available in station a
	tcb=0 # trains available in station b
	
	ltca=0 # lowest train deficit at station a
	ltcb=0 # lowest train deficit at station b
	for h in range(24):
		for m in range (60):
			ctime="%02d:%02d" % (h, m)
			if m-turnaround<0:
				mt=m-turnaround+60
				ht=h-1
			else:
				mt=m-turnaround
				ht=h
			ttime="%02d:%02d" % (ht, mt)
			if a2bl.count(ctime)!=0: 
				tca=tca-a2bl.count(ctime); 
				for i in range(a2bl.count(ctime)): 
					a2bl.remove(ctime)
			if a2ba.count(ttime)!=0: 
				tcb=tcb+a2ba.count(ttime); 
				for i in range(a2ba.count(ttime)): 
					a2ba.remove(ttime)
			if b2al.count(ctime)!=0: 
				tcb=tcb-b2al.count(ctime); 
				for i in range(b2al.count(ctime)): 
					b2al.remove(ctime)
			if b2aa.count(ttime)!=0: 
				tca=tca+b2aa.count(ttime); 
				for i in range(b2aa.count(ttime)): 
					b2aa.remove(ttime)
			
			if tca<ltca:
				ltca=tca
			if tcb<ltcb:
				ltcb=tcb
			#print ctime, ttime, tca, tcb
	if ltca<0:
		tna=ltca*-1
	else:
		tna=0
	if ltcb<0:
		tnb=ltcb*-1
	else:
		tnb=0
	#print a2bl, a2ba, b2al, b2aa
	return tna, tnb


if __name__ == '__main__':
	fileHandle = open('large.in')
	fileOut=open('output','w')
	N = int(fileHandle.readline())	
	for n in range(N):
		c=main(fileHandle)
		fileOut.write("Case #"+str(n+1)+": "+str(c[0])+" "+str(c[1])+"\n")
	fileHandle.close()
	fileOut.close()