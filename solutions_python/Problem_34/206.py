#!/usr/bin/python

import sys, os, string, re

in_file = sys.stdin
groups = in_file.readline().split()
D = int(groups[1])
N = int(groups[2])

words = []
for i in range(D):
	words.append(in_file.readline().strip())

for i in range(N):
	pattern = in_file.readline().strip()
	pattern = re.sub('\(', '[', pattern)
	pattern = re.sub('\)', ']', pattern)
	pattern += '$'
	regex = re.compile(pattern)
	ct = 0
	for word in words:
		if regex.match(word):
			ct += 1
	print 'Case #'+str(i+1)+': '+str(ct)
