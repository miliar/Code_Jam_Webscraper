import itertools

boards = []

n = int(raw_input())

for i in range(n):
	board = [0] * 16

	board[0], board[1], board[2], board[3] = list(raw_input())
	board[4], board[5], board[6], board[7] = list(raw_input())
	board[8], board[9], board[10], board[11] = list(raw_input())
	board[12], board[13], board[14], board[15] = list(raw_input())
	empty = raw_input()

	boards.append(board)

print boards

horizontal = [(0,1,2,3), (4,5,6,7), (8,9,10,11), (12,13,14,15)]
vertical = [(0,4,8,12), (1,5,9,13), (2,6,10,14), (3,7,11,15)]
diagonal = [(0,5,10,15), (3,6,9,12)]

def isWin(board, combo):
	temp = board[combo[0]] + board[combo[1]] + board[combo[2]] + board[combo[3]]
	if ('.' not in temp) and not ('X' in temp and 'O' in temp):
		return 'X' if 'X' in temp else 'O'
	else:
		return False


def isDraw(board):
	print board
	return '.' not in board

for i in range(len(boards)):
	for combo in itertools.chain(horizontal, vertical, diagonal):
		a = isWin(boards[i], combo)
		if a:
			print "Case #%s: %s won" % (i+1, a)
			break
	else:
		if isDraw(boards[i]):
			print "Case #%s: Draw" % (i+1)	
		else:
			print "Case #%s: Game has not completed" % (i+1)