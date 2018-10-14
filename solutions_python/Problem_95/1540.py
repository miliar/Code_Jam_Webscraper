#!/usr/bin/env python
# encoding: utf-8
"""
speaking_in_tongues.py

Created by Yue Zhang on 2012-04-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

def read_input(contain, file_name):
	source = open(file_name, 'r')
	i = 0
	for line in source:
		i += 1
		if i == 1: 
			total = int(line.rstrip())
			continue
		else:
			contain.append(line.rstrip())
	return total

def main():
	result = file('result', 'w')
	for i in range(total):
		ms = map_source[i]
		mr = map_result[i]
		for j in range(len(ms)):
			if mapping.has_key(ms[j]):
				continue
			else:
				mapping[ms[j]] = mr[j]
	count = 1
	for sentence in trans:
		result.write('Case #')
		result.write(str(count))
		result.write(': ')
		for letter in sentence:
			result.write(mapping[letter])
		result.write('\n')
		count += 1


if __name__ == '__main__':
	mapping = {'q': 'z', 'z': 'q'}
	trans, map_source, map_result = [], [], []
	read_input(trans, 'origins')
	total = read_input(map_source, 'input.txt')
	read_input(map_result, 'output.txt')	
	main()	
#	print trans, map_source, map_result
#	print mapping

