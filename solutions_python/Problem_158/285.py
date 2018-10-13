#!/usr/bin/env python
import sys

X = 0
R = 0
C = 0

def process():
	rlt = 'RICHARD'
	if (R * C) % X <> 0:
		return rlt
		
	if X == 1 or X == 2:
		rlt = 'GABRIEL'
	elif X == 3 and min(R, C) >= 2:
		rlt = 'GABRIEL'
	elif (X == 4 or X == 5) and min(R, C) >= 3:
		rlt = 'GABRIEL'
	elif X == 6 and min(R, C) >= 4:
		rlt = 'GABRIEL'
	
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	X, R, C = map(int, input_file.readline().split())
	
	print 'Case #%d:' % (i + 1), process()