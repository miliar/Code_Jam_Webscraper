"""
	chipjacks
	Google CodeJam 2013
	Problem A - Tic-Tac-Toe-Tomek
"""

import sys

f = open('A-small.in', 'r')
T = int(f.readline())	# num test cases

for t in range(1, T+1):
	winner = 'u'	#unknown winner
	board = [list(f.readline().strip()) for i in range(4)]

	f.readline()

	#check horizontals
	for i in range(4):
		#for each horizontal
		first = board[i][0]
		if first == '.':
			continue
		for c in board[i]:
			if c != first and c != 'T':
				break
		else:
			winner = first
		if winner != 'u':
			break

	if winner != 'u':
		print("Case #{}: {} won".format(t, winner))
		continue

	#check verticles

	#transpose board
	board = list(zip(*board))
	for i in range(4):
		first = board[i][0]
		if first == '.':
			continue
		for s in board[i]:
			if s != first:
				break
		else:
			winner = first
		if winner != 'u':
			break

	if winner != 'u':
		print("Case #{}: {} won".format(t, winner))
		continue

	#check first diagonal
	first = board[0][0]
	if first == 'T':
		first = board[1][1]
	if first != '.':
		for i in range(1, 4):
			if board[i][i] != first and board[i][i] != 'T':
				break
		else:
			winner = first

	if winner != 'u':
		print("Case #{}: {} won".format(t, winner))
		continue

	#check second diagonal
	first = board[0][3]
	if first == 'T':
		first = board[1][2]
	if first != '.':
		for i in range(1, 4):
			if board[i][3-i] != first and board[i][3-i] != 'T':
				break
		else:
			winner = first

	found = False
	if winner != 'u':
		print("Case #{}: {} won".format(t, winner))
		continue
	else:
		for c in [c for row in board for c in row]:
			if c == '.':
				print("Case #{}: Game has not completed".format(t))
				break
		else:
			print("Case #{}: Draw".format(t))

