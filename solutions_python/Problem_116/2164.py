#!/usr/bin/python

f = open("A-large.in", "r")

T = int(f.readline())

def winner(line):
	if '.' in line:
		return '.'
	if line == 'XXXX':
		return 'X'
	elif line == 'OOOO':
		return 'O'
	elif 'T' in line:
		if line.count('X') == 3:
			return 'X'
		elif line.count('O') == 3:
			return 'O'
	

for t in range(1, T+1):

	board = {}

	for i in range(4):
		row = f.readline().strip()
		for j in range(4):
			board[i,j] = row[j]

	f.readline()

	res = []
	for i in range(4):
		res.append(winner(board[i,0]+board[i,1]+board[i,2]+board[i,3]))
	for j in range(4):
		res.append(winner(board[0,j]+board[1,j]+board[2,j]+board[3,j]))

	res.append(winner(board[0,0]+board[1,1]+board[2,2]+board[3,3]))
	res.append(winner(board[3,0]+board[2,1]+board[1,2]+board[0,3]))

	if 'X' in res:
		print "Case #{0}: X won".format(t)
	elif 'O' in res:
		print "Case #{0}: O won".format(t)
	elif '.' in res:
		print "Case #{0}: Game has not completed".format(t)
	else:
		print "Case #{0}: Draw".format(t)

