#!/usr/bin/env python
# encoding: utf-8
"""
problemA.py

Created by Marcel Caraciolo on 2010-05-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	lines = [  line.strip()  for line in open('A-large.in')]
	#TestCases
	T = int(lines[0])
	if  T > 10000 or T < 1:
		exit()
	l = 1
	
	otF = open('A-large.out','w')
	number = 1
	while l <= T:
		#GET THE SNNAPERS
		N,K = map(int,lines[l].split(' '))
		if N > 30 or N < 1:
			exit()
		if K > 100000000 or K < 0:
			exit()
		
		maxNumber = 2 ** N
		v = ''
		if K % (maxNumber) == (maxNumber-1):
			v =  'ON'
		else:
			v = 'OFF'
		l+=1
		otF.write('Case #%d: %s\n' %(number,v))
		number+=1
	otF.close()
if __name__ == '__main__':
	main()

