#!/usr/bin/env python

import sys


T = int(sys.stdin.readline())

for i in range(T):
    
	a = int(sys.stdin.readline())

	for k in range(a-1):
		sys.stdin.readline()

	aLine = sys.stdin.readline()

	for k in range(4-a):
		sys.stdin.readline()

	aLine = aLine.split()

	b = int(sys.stdin.readline())

	for k in range(b-1):
		sys.stdin.readline()

	bLine = sys.stdin.readline()
	bLine = bLine.split()

	for k in range(4-b):
		sys.stdin.readline()

	intr = list(set(aLine) & set(bLine))

	out = "Case #%d: " % (i+1)

	if len(intr) == 0:
		out += "Volunteer cheated!"
	elif len(intr) == 1:
		out += intr[0]
	else:
		out += "Bad magician!"


	print(out)