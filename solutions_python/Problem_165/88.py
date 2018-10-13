#!/usr/bin/env python
import sys

R = 0
C = 0
W = 0

def process():
	m = 0
	if C % W == 0:
		m = 1
	rlt = C / W * R + W - m
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	R, C, W= map(int, input_file.readline().split())
	print 'Case #%d:' % (i + 1), process()