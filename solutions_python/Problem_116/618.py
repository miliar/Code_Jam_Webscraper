#!/usr/bin/python2
from __future__ import print_function

import sys

def check(line):
	#print('checking', line)
	last = line[0]
	count = 0
	for x in line:
		if x == last or x == 'T': count += 1
		if x in 'XO': last = x
	if count == 4 and last != '.':
		return last

def solve():
	lines = []
	for _ in range(4):
		lines.append(sys.stdin.readline().strip())
	sys.stdin.readline()
	#print("lines:", lines)
	# check h lines
	win = None
	for i in range(4):
		win = win or check(lines[i])
	# check v lines
	for i in range(4):
		win = win or check([lines[j][i] for j in range(4)])
	# check \ diag
	win = win or check([lines[i][i] for i in range(4)])
	# check / diag
	win = win or check([lines[i][3-i] for i in range(4)])

	if win:
		return win + " won"
	else:
		if ''.join(lines).count('.') == 0:
			return "Draw"
		else:
			return "Game has not completed"

n = int(sys.stdin.readline())
for i in range(n):
	result = solve()
	print("Case #%s: %s" % (i+1, result))
