#!/usr/bin/env python
import sys

audience = []
smax = 0

def process():
	rlt = 0
	stood = 0
	for i in range(0, smax):
		if audience[i] == 0:
			continue
		while stood < i:
			rlt += 1
			stood += 1
		stood += audience[i]
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	tmp = input_file.readline().split()
	smax = int(tmp[0]) + 1
	audience = []
	for j in tmp[1]:
		audience.append(int(j))
	
	print 'Case #%d:' % (i + 1), process()