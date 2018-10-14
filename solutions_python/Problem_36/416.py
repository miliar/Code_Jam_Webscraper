#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Keishi Hattori on 2009-09-03.
Copyright (c) 2009 Keishi Hattori. All rights reserved.
"""

import sys
import os
import re

wtcj = "welcome to code jam"

def solve(s, i):
	"""docstring for removeUnnecessaryChars"""
	if (i >= len(wtcj)) :
		return 1
	ans = 0
	for j in range(len(s)) :
		if (s[j] == wtcj[i]) :
			ans += solve(s[j + 1 :], i + 1)
	return ans

def removeUnnecessaryChars(str):
	"""docstring for removeUnnecessaryChars"""
	return re.sub(r'[^welcom tdja]', '', str)

def main():
	line = sys.stdin.readline()
	if not line:
		raise Exception('No More Lines')
	N = int(line) # number of test cases
	for i in range(N) :
		line = sys.stdin.readline()
		if not line:
			raise Exception('No More Lines')
		s = removeUnnecessaryChars(line[:-1])	
		a = solve(s, 0)
		print "Case #%d: %04d" % (i+1, a)
	pass


if __name__ == '__main__':
	main()
