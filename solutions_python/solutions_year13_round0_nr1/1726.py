def determine(line):
	base = 'T'
	for c in line:
		if c == '.':
			return None
		if c == base:
			continue # we're good, move on to the next character
		else:
			if base == 'T':
				base = c # update base to the actual player
			elif c == 'T':
				continue # T is OK, just go for the next one
			else:
				return None # no one wins
	return base # the winner

def checkboard(board):
	# board should be sth like ['XXX.', '....', 'OOXO', '....']
	for j in range(4):
		r = determine(board[j]) # row
		if r is not None:
			return r
		r = determine((board[0][j], board[1][j], board[2][j], board[3][j])) # column
		if r is not None:
			return r

	# 2 diagonal
	r = determine((board[0][0], board[1][1], board[2][2], board[3][3]))
	if r is not None:
		return r
	r = determine((board[0][3], board[1][2], board[2][1], board[3][0]))
	if r is not None:
		return r

	# if we're here, which means no one wins, scan for '.' to tell if the game's finished or not
	for j in range(4):
		if board[j].find('.') >= 0:
			return '.' # unfinished
	
	return None # draw

# starts here
import sys
l = sys.stdin.readline()
count = int(l)

results = []
for i in range(count):
	board = []
	for j in range(4): # 4 lines each input
		line = sys.stdin.readline().rstrip()
		board.append(line)
	
	results.append(checkboard(board))
	sys.stdin.readline() # eat the empty line

# print results
for i in range(count):
	if results[i] == 'X' or results[i] == 'O':
		msg = results[i] + ' won'
	elif results[i] == '.':
		msg = 'Game has not completed'
	else: # draw
		msg = 'Draw'
	print 'Case #' + str(i+1) + ": " + msg
