import sys

def rotate(board):
	newBoard = []
	num = len(board)
	for i in range(num):
		newBoard.append(range(num))
	
	for i in range(num):
		for j in range(num):
			newBoard[i][j] = board[num - j - 1][i]
	return newBoard

def drop(board):
	num = len(board)
	for i in range(num,-1,-1):
		for j in range(num):
			index = i 
			while index + 1 < num and board[index + 1][j] == '.':
				index = index + 1
			if (index is not i):
				board[index][j] = board[i][j]
				board[i][j] = '.'
	for row in board:
		line = ''
		for item in row:
			line = line + item
		print line
			

def check(board, require):
	num = len(board)
	maxR = 0
	maxB = 0
	for i in range(num):
		for j in range(num):
			if board[i][j] is not '.':
				tempCount = count(board, i, j)
				if (board[i][j] == 'R') and tempCount > maxR:
					maxR = tempCount
				if (board[i][j] == 'B') and tempCount > maxB:
					maxB = tempCount
	print 'maxR is:', maxR, 'maxB is:', maxB
	if maxR >= require:
		if maxB >= require:
			return 'Both'
		else:
			return 'Red'
	elif maxB >= require:
		return 'Blue'
	else:
		return 'Neither'
		

def count(board, i, j):
	maxCount = 0
	num = len(board)
	color = board[i][j]
	#go right
	index = j
	while index+1 < num and board[i][index+1] == color:
		index = index + 1
	if index - j + 1 > maxCount:
		maxCount = index -j + 1
	
	#go down
	index = i
	while index - 1 >= 0 and board[index - 1][j] == color:
		index = index - 1
	if i - index + 1 > maxCount:
		maxCount = i - index + 1
	
	#go updiagnoal
	index = i
	index_1 = j
	while (index < num - 1) and (index_1 < num -1) and board[index + 1][index_1 + 1] == color:
		index = index + 1
		index_1 = index_1 + 1
	if index_1 - j + 1 > maxCount:
		maxCount = index_1 - j + 1
	
	#go downdiagnoal
	index = i 
	index_1 = j
	while (index - 1 >=0 ) and (index_1 < num - 1) and board[index - 1][index_1 + 1] == color:
		index = index - 1
		index_1 = index_1 + 1
	if index_1 - j + 1 > maxCount:
		maxCount = index_1 - j + 1
	
	return maxCount
			
if __name__ == "__main__":
	inFile = open(sys.argv[1])
	outFile = open(sys.argv[2],'w')
	testCaseNum = int(inFile.readline())
	for i in range(testCaseNum):
		(n,k) = [int(x) for x in inFile.readline().split(' ')]
		board = []
		for j in range(n):
			board.extend(inFile.readline().split(' '))
		newBoard = rotate(board)
		drop(newBoard)
		outFile.write('Case #' + str(i+1) + ': ' + str(check(newBoard,k)) + '\n')
	
	outFile.close()
	inFile.close()
		
			
	
	
