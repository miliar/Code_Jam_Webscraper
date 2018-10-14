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

def solve(L, dictionary, case):
	"""docstring for matches"""
	n = 0
	template = []
	for i in range(L) :
		template.append([])
		if case[n] == '(' :
			while True :
				n += 1
				if case[n] == ')' :
					n += 1
					break
				else :
					template[i].append(case[n])
		else :
			template[i].append(case[n])
			n += 1
	ans = 0
	for d in dictionary :
		for i in range(L) :
			try:
				template[i].index(d[i])
				if i == L - 1 :
					ans += 1
			except Exception, e:
				break
	return ans

def solveCase(L, dictionary, case):
	"""docstring for solveCase"""
	if len(case) == L:
		try:
			dictionary.index(case)
			return 1
		except Exception, e:
			return 0
	p = re.compile('\((.+?)\)')
	m = p.search(case)
	if not m :
		return 0
	possibilities = m.group(1)
	ans = 0
	for i in range(len(possibilities)) :
		start = m.start() - 1
		if start < 0 :
			start = 0
		s = case[:m.start()] + possibilities[i] + case[m.end():]
		ans += solveCase(L, dictionary, s)
	return ans

def main():
	line = sys.stdin.readline()
	if not line:
		raise Exception('No More Lines')
	parts = line.split()
	L = int(parts[0]) # word length
	D = int(parts[1]) # number of words in this language
	N = int(parts[2]) # number of test cases
	dictionary = []
	for i in range(D) :
		line = sys.stdin.readline()
		if not line:
			raise Exception('No More Lines')
		dictionary.append(line[:-1])
	for i in range(N) :
		line = sys.stdin.readline()
		if not line:
			raise Exception('No More Lines')
		a = solve(L, dictionary, line[:-1])
		print "Case #%d: %d" % (i+1, a)
	pass


if __name__ == '__main__':
	main()
