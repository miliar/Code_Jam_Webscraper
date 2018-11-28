class TicTacToe:
	FREE = 'T'
	boards = []
	
	def __init__(self, boardList):
		self.boards = boardList	
		self.processAllBoards()
	
	def processAllBoards(self):
		for i, board in enumerate(self.boards):
			print 'Case #%d:' % (i+1),
			self.determineWinner(board)
			
	def determineWinner(self, board):
		for row in board:
			if self.winsRow(row, 'X'):
				print 'X won'
				return
			elif self.winsRow(row, 'O'):
				print 'O won'
				return
		for i in range(0, 4):
			if self.winsColumn(board, i, 'X'):
				print 'X won'
				return
			elif self.winsColumn(board, i, 'O'):
				print 'O won'
				return
		if self.winsDiagonal(board, 'X'):
			print 'X won'
			return
		elif self.winsDiagonal(board, 'O'):
			print 'O won'
			return
		if self.boardFull(board):
			print 'Draw'
		else:
			print 'Game has not completed'
				
				
	def winsRow(self, row, player):
		valid = [player, self.FREE]
		if row[0] in valid and row[1] in valid and row[2] in valid and row[3] in valid:
			return True
		return False
			
	def winsColumn(self, board, col, player):
		valid = [player, self.FREE]
		for row in board:
			if row[col] not in valid:
				return False;
		return True
		
	def winsDiagonal(self, board, player):
		valid = [player, self.FREE]
		if board[0][0] in valid and board[1][1] in valid and board[2][2] in valid and board[3][3] in valid:
			return True
		elif board[0][3] in valid and board[1][2] in valid and board[2][1] in valid and board[3][0] in valid:
			return True
		return False
		
	def boardFull(self, board):
		for row in board:
			for col in row:
				if col == '.':
					return False
		return True


def parseInputToBoards(inputFile):
	lines = [line.strip() for line in open(inputFile)]
	boards = []
	numBoards = int(lines[0])
	
	for i in range(numBoards):
		startingLineForBoard = i*5+1
		boards.append(addBoard(lines[startingLineForBoard:startingLineForBoard+4]))
		
	return boards

def addBoard(lines):
	board = []
	for line in lines:
 		board.append(addRow(line))
 	return board
		
def addRow(line):
	row = []
	for c in line:
		row.append(c)
	return row
			

boards = parseInputToBoards('A-Large.in')

TicTacToe(boards)