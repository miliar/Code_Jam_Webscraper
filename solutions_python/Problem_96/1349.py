#!/usr/bin/env python
# encoding: utf-8
"""
dance.py

Created by Yue Zhang on 2012-04-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import math

def read_input():
	source = open('input', 'r')
	i = 0
	for line in source:
		i += 1
		if i == 1: 
			total = int(line.rstrip())
			continue
		else:
			arr = line.rstrip().split()
			arr = [int(a) for a in arr]
			tmp = {'N': arr[0], 'S': arr[1], 'p': arr[2], 'ts': arr[3:]}
			judges.append(tmp)
#	return total

def main():
	results = []
	result = file('output', 'w')
	i = 1
	for judge in judges:
		p = judge['p']
		s = judge['S']
		ts = judge['ts']
		count, sur = 0, 0
		print i, "P:", p, ", S:", s, ', TS:', ts
		for ti in ts:
			first, second, last = 0, 0, 0
			if ti > p * 3: 
				first = ti / 3
				remain = ti - first
				second = remain / 2
				last = remain - second
				if (math.fabs(first - second) == 2 or \
				math.fabs(first - last) == 2 or \
				math.fabs(last - second) == 2) and sur < s:
					sur += 1
					count += 1	
				else: 
					count += 1
				print "  c1", ti, first, second, last
			else:
				remain = ti - p
				if remain > 0: first = p
				if remain < 0: remain = 0
				second = remain / 2
				last = remain - second
				if first == p:
					if first - second == 2 and sur < s:
						sur += 1
						count += 1
					if first - second <= 1:
						count += 1
				print "  c2", ti, first, second, last
		result.write('Case #')
		result.write(str(i))
		result.write(': ')
		result.write(str(count))
		result.write('\n')
		print " ", count
		i += 1
	pass


if __name__ == '__main__':
	judges = []
	read_input()
	main()
#	print judges

