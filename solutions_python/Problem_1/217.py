#!/usr/bin/env python
# encoding: utf-8
"""
script.py

Created by Vladimir Prudnikov on 2008-07-17.
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
		
		S = int(f.readline().strip())
		se = [f.readline().strip() for i in xrange(S)]
		
		Q = int(f.readline().strip())
		queries = [f.readline().strip() for i in xrange(Q)]

		data = {}
		for se_ in se:
			data[se_]=0
		
		prev_q = None
		for q in queries:
			# print q
			new_val = min(data.values()) + 1
			for s in se:
				if prev_q == s or q == s:
					data[q] = new_val
					if prev_q:
						data[prev_q] = new_val
			
			prev_q = q
			# print data

		result = min(data.values())
		print "Case #%s: %s" % (case, result)
		case = case + 1
	
	f.close()

	
if __name__ == '__main__':
	main()

