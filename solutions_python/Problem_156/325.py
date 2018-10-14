#!/usr/bin/env python
import sys

D = 0
P = []

def process():
	max_P = max(P)
	rlt = max_P
	for x in range(2, max_P):
		spec = 0
		for i in P:
			tmp = i / x
			if i % x == 0:
				tmp -= 1
			spec += tmp
		if spec <> 0:
			tmp = x + spec
			if tmp < rlt:
				rlt = tmp
		
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	D = int(input_file.readline())
	P = map(int, input_file.readline().split())
	
	print 'Case #%d:' % (i + 1), process()