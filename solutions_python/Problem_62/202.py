#!/usr/bin/env python
# encoding: utf-8
"""
1CA.py

Created by Lisbeth Nilsen on 2010-05-22.
To run, download Python 2.6 interpreter from http://python.org/
"""

import sys
import os

def intersects(wire1, wire2):
	(a1, b1) = wire1
	(a2, b2) = wire2
	if(a1 < a2 and b1 > b2):
		return True
	elif(a1 > a2 and b1 < b2):
		return True
	else:
		return False
		

def calc(f):     
	result = 0
	num = int(f.readline().split()[0]) 		
	wires = {}
	for i in range(num):
		(a, b) = f.readline().split()
		newwire = (int(a), int(b))

		for a2, b2 in wires.iteritems():
			if intersects(b2, newwire):
				result += 1
			
		wires[int(a)] = newwire
		
	return result
	
		
		

f = open('A-large.in', 'r')
lines = f.readline()   

c = int(lines.split()[0])
         
of = open('output_a_large.txt', 'w')

for idx in range(c):
	of.write('Case #%(idx)i: %(i)i\n' % {'idx': idx + 1, 'i': calc(f)})                          
   
f.close()
of.close()