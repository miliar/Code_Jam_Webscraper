#!/usr/bin/env python
# encoding: utf-8
"""
recycle.py

Created by Yue Zhang on 2012-04-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

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
			tmp = {'s': arr[0], 'e': (arr[1] + 1)}
			items.append(tmp)

def main():
	def get_power(n):
		power = 1
		while 10 * power < n:
			power *= 10;
		return power
	def permutation(n):
		temp = []
		power = get_power(n)
		i, cur = 0, 0
		if n % power == 0:
			return temp
		while not cur == n :
			if i == 0: cur = n
			base = 10
			first = cur / base
			remain = cur % base
			while remain == 0: 
				base *= 10
				first = cur / base
				remain = cur % base
			if base == 10:
				cur = remain * power + first
			else:
				cur = remain * get_power(first) * 10 + first
#			print cur, first, remain, base, power
			if not cur == n: temp.append(cur)
			i += 1
#		print temp
		return temp
	result = file('output', 'w')
	seq = 1
	for item in items:
		count = 0
		start, end = item['s'], item['e']
		for i in range(start, end):
			for r in permutation(i):
				if r in range(item['s'], item['e']):
					count += 1
					continue
		result.write('Case #')
		result.write(str(seq))
		result.write(': ')
		result.write(str(count/2))
		result.write('\n')
		seq += 1
	pass


if __name__ == '__main__':
	items = []
	read_input()
	main()
