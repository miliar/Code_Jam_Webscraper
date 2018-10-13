filename = 'B-large.in'
f = open(filename,'r')

n = int(f.readline())

def isGood(board,x,y):
	#print board,x,y
	if x == 1:
		return True
	if y == 1:
		return True
	minVal = 10000000
	minRow = -1
	minCol = -1
	for row in range(0,x):
		for col in range(0,y):
			if board[row][col] < minVal:
				minRow = row
				minCol = col
				minVal = board[row][col]

	row = board[minRow]
	col = zip(*board)[minCol]
	
	rowSum = sum([z != minVal for z in row])
	colSum = sum([z != minVal for z in col])
	#print x,y,minRow,minCol,rowSum,colSum
	
	if rowSum > 0 and colSum > 0:
		return False
	
	if rowSum == 0:
		#delete the row
		newBoard = board[0:minRow]
		newBoard += board[minRow+1:]
		return isGood(newBoard,x-1,y)

	if colSum == 0:
		#delete the column
		boardt = [[board[i][j] for i in range(len(board))] for j in range(len(board[0]))]
		newBoard = boardt[0:minCol]
		newBoard += boardt[minCol+1:]
		return isGood(newBoard,y-1,x)

for i in range(1,n+1):
	dims = f.readline().strip()
	x = int(dims.split(' ')[0])
	y = int(dims.split(' ')[1])
	board = []
	for k in range(0,x):
		line = f.readline().strip()
		arr = map(lambda x:int(x),line.split(' '))
		board.append(arr)
	
	if isGood(board,x,y):
		print 'Case #'+str(i)+': YES'
	else:
		print 'Case #'+str(i)+': NO'


