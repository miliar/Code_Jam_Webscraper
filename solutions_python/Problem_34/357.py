#!/usr/bin/python

import sys, re

def getl():
	return sys.stdin.readline().rstrip()

l, d, n = [int(x) for x in  getl().split()]
words = []

for i in range(d):
	words.append(getl())

for i in range(n):
	pattern = re.compile(getl().replace('(', '[').replace(')', ']'))
	counter = 0
	for word in words:
		if pattern.match(word):
			counter += 1
	print('Case #{0}: {1}'.format(i+1, counter))
