import sys

def check(char, board):
	dcount1 = 0
	dcount2 = 0
	for i in xrange(4):
		vcount = 0
		hcount = 0
		for j in xrange(4):
			if board[i][j] in char + 'T':
				vcount += 1
			if board[j][i] in char + 'T':
				hcount += 1
		if vcount == 4 or hcount == 4:
			return True
		if board[i][i] in char + 'T':
			dcount1 += 1
		if board[4-i-1][i] in char + 'T':
			dcount2 += 1
	if dcount1 == 4 or dcount2 == 4:
		return True
	return False

games = int(sys.stdin.readline())
for i in xrange(1, games+1):
	board = []
	outcome = "Draw"
	for j in xrange(4):
		board.append(sys.stdin.readline().strip())
	if check('X', board):
		outcome = 'X won'
	if check('O', board):
		outcome = 'O won'
	if 'won' not in outcome:
		for line in board:
			if '.' in line:
				outcome = "Game has not completed"
	print "Case #%d: %s" % (i, outcome)
	sys.stdin.readline()
