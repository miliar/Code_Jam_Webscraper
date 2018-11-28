#!/usr/bin/env python

import sys


T = int(sys.stdin.readline())

for case in range(0, T):
	grid0 = list()
	grid1 = list()
	num0 = int(sys.stdin.readline())
	for i in range(0, 4):
		row = sys.stdin.readline().split()
		row = [int(x) for x in row]
		grid0.append(row)

	num1 = int(sys.stdin.readline())
	for i in range(0, 4):
		row = sys.stdin.readline().split()
		row = [int(x) for x in row]
		grid1.append(row)

	row0 = grid0[num0-1]
	row1 = grid1[num1-1]
	
	match = 0
	for card in row0:
		if card in row1:
			match = match + 1
			result = str(card)

	if match == 0:
		result = "Volunteer cheated!"
	elif match > 1:
		result = "Bad magician!"

	print "Case #%s: %s" % (str(case+1), result )
