#!/usr/bin/python

import sys, os, string, re

in_file = sys.stdin
N = int(in_file.readline())

for i in range(N):
	text = in_file.readline().strip()
	text_len = len(text)
	sums = text_len*[0]
	for pos in range(text_len):
		if text[pos] == 'w':
			sums[pos] = 1
	for ch in 'elcome to code jam':
		prev_sums = sums
		sums = text_len*[0]
		sum = 0
		for pos in range(text_len):
			if text[pos] == ch:
				sums[pos] = sum%10000
			sum += prev_sums[pos]
	sum = 0
	for t in sums:
		sum += t
	print 'Case #%d: %04d' % (i+1, sum%10000)
