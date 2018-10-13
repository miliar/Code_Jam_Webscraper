#!/usr/bin/python
# dirty and inefficient solution, this is a rush
import sys
T = int(sys.stdin.readline().strip())
for t in range(1, T + 1):
	row = int(sys.stdin.readline().strip())
	board = [[int(x) for x in sys.stdin.readline().strip().split()]]
	for i in range(3):
		board.append([int(x) for x in sys.stdin.readline().strip().split()])
	possibles = board[row - 1]
	
	row = int(sys.stdin.readline().strip())
	board = [[int(x) for x in sys.stdin.readline().strip().split()]]
	for i in range(3):
		board.append([int(x) for x in sys.stdin.readline().strip().split()])
	secondrow = board[row - 1]
	commun = []
	for c in possibles:
		if c in secondrow:
			commun.extend([c])	
	resp = "Bad magician!"
	if len(commun) == 0:
		resp = "Volunteer cheated!"
	elif len(commun) == 1:
		resp = commun[0]
	print "Case #{t}: {resp}".format(t=t, resp=resp)