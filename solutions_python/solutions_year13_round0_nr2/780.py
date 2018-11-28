#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
	input = sys.argv[1]
else:
	input = "input.txt"

try:
	with open(input) as f:
		content = [[int(c) for c in line.split()] for line in f.readlines()]
except:
	print("Can not find input file: %s" % input)
	sys.exit()

T = int(content[0][0])

case = 1
line = 1
while case <= T:
	N, M = content[line]
	lawn = content[line+1:line+N+1]

	result = None
	try:
		for i in range(N):
			for j in range(M):
				h = lawn[i][j]
				
				if (max([lawn[i2][j] for i2 in range(N)]) > h and max([lawn[i][j2] for j2 in range(M)]) > h):
					result = False
					raise
	except:
		pass

	if result == False:
		result = "NO"
	else:
		result = "YES"
	
	print("Case #%d: %s" % (case, result))

	case += 1
	line += N + 1
