def readInput():
	f = open('A-small-attempt0.in', 'r')
	
	n = int(f.readline().strip())
	
	boards = []
	board = []
	for line in f:
		if len(board) == 4:
			boards.append(board)
			board = []
		line = line.strip()
		if len(line) > 0:
			board.append(line)

	return boards

def asd(b):
	if b == 'X':
		return "1"
	if b == 'T':
		return "2"
	return "0"

def processBoard(board):
	for i in range(0, 4):
		if reduce (lambda a,b: a and b, [c == 'X' or c == 'T' for c in board[i]]):
			return "X won"
		if reduce (lambda a,b: a and b, [c == 'O' or c == 'T' for c in board[i]]):
			return "O won"
		
		col = [row[i] for row in board]
		if reduce (lambda a,b: a and b, [c == 'X' or c == 'T' for c in col]):
			return "X won"
		if reduce (lambda a,b: a and b, [c == 'O' or c == 'T' for c in col]):
			return "O won"
		
	d = [board[i][i] for i in range(0, 4)]
	print d
	if reduce (lambda a,b: a and b, [c == 'X' or c == 'T' for c in d]):
		return "X won"
	if reduce (lambda a,b: a and b, [c == 'O' or c == 'T' for c in d]):
		return "O won"
	
	d = [board[i][3 - i] for i in range(0, 4)]
	print d
	if reduce (lambda a,b: a and b, [c == 'X' or c == 'T' for c in d]):
		return "X won"
	if reduce (lambda a,b: a and b, [c == 'O' or c == 'T' for c in d]):
		return "O won"

	if reduce (lambda a,b: a == 0 and b == 0, [len([c for c in row if c == '.']) for row in board]):
		return "Draw"
		
	return "Game has not completed"

boards = readInput()
results = []
i = 1
for board in boards:
	results.append('Case #' + str(i) + ': ' + processBoard(board) + '\n')
	i = i + 1
	
f = open('A-small-attempt0.out', 'w')
f.writelines(results)
f.close()