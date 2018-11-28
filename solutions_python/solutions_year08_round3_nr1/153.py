#!/usr/bin/env python
# encoding: utf-8
"""
script.py

Created by Vladimir Prudnikov on 2008-07-27.
Copyright (c) 2008 Prudnikov Vladimir. All rights reserved.

Made on 
"""

import sys
import os
import math

def main():
	input_filename = sys.argv[1]
	f = open(input_filename)
	count = int(f.readline().strip())
	case = 1
	for i in xrange(count):
		
		P, K, L = f.readline().strip().split(' ')
		P = int(P)
		K = int(K)
		L = int(L)
		a = f.readline().strip().split(' ')
		for i in xrange(len(a)):
			a[i] = int(a[i])
		
		a.sort()
		# a.reverse()
		
		buttons = []
		ln = 1
		
		
		for i in xrange(K):
			buttons.append([])
			
		
		for j in xrange(P):
			for i in xrange(K):
				try:
					buttons[i].append(a.pop())
				except IndexError:
					break


		result = 0
		for but in buttons:
			but = list(but)
			but.sort()
			but.reverse()
			# print but
			for k in xrange(len(but)):
				# print k
				# print but[k], k+1
				result = result + but[k]*(k+1)
		
		print "Case #%s: %s" % (case, result)
		case = case + 1
	f.close()

	
if __name__ == '__main__':
	main()

