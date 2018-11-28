#!/usr/bin/env python
# encoding: utf-8
"""
1BA.py

Created by Lisbeth Nilsen on 2010-05-22.
To run, download Python 2.6 interpreter from http://python.org/
"""

import sys
import os

def calc(f):
	result = 0
	(n, m) = f.readline().split()
	print n, m
	dirs = ["/"]
	
	#Initial directories
	for i in range(int(n)):
		dirs.append(f.readline().strip())      		
	#print dirs
	
	#New directories
	for i in range(int(m)):
		newDir = f.readline().strip()
		newDirs = newDir.split('/')
		#print newDirs
		#Skip first, empty string
		for d in range(1, len(newDirs) + 1):
			#print "Checking:", d, "/".join(newDirs[1:d])
			if "/" + "/".join(newDirs[1:d]) in dirs:
				pass #print "/" + "/".join(newDirs[1:d]), "in dirs"
			else:
				result += 1
				dirs.append("/" + "/".join(newDirs[1:d]))
				#print "/" + "/".join(newDirs[1:d]), "added to dirs"
	#print dirs		
	return result
	
		
		

f = open('A-large.in', 'r')
lines = f.readline()   

c = int(lines.split()[0])

                       
of = open('output_a_large.txt', 'w')

for idx in range(c):
	of.write('Case #%(idx)i: %(i)i\n' % {'idx': idx + 1, 'i': calc(f)})                          
  
f.close() 
of.close()