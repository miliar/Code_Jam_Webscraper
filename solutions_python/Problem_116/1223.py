from sys import stdin

def winner(arr):
	for char in "X", "O":
		if 4 == sum([1 if char == arr[x] or "T" == arr[x] else 0 for x in range(len(arr))]):
			return char + " won"
	return None

def status(board):
	for i in range(4):
		w = winner(board[i])
		if w: return w
		w = winner([board[x][i] for x in range(4)])
		if w: return w
	w = winner([board[x][x] for x in range(4)])
	if w: return w
	w = winner([board[3-x][x] for x in range(4)])
	if w: return w
	for i in range(4):
		for j in range(4):
			if board[i][j] == ".":
				return "Game has not completed"
	return "Draw"

input = stdin.readlines()
T = int(input[0])

for i in range(T):
	board = []
	for j in range(4):
		board.append(input[i*5+j+1][:-1])
	#print board
	print "Case #{0}: {1}".format(i+1, status(board))