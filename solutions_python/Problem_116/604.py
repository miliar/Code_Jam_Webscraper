import copy
import unittest

# Board size
N = 4

# Board symbol
T = 'T'
X = 'X'
O = 'O'
EMPTY = '.'

# Messages
XWIN = "X won"
OWIN = "O won"
DRAW = "Draw"
NOTOVER = "Game has not completed"

def readInput(filename):
	'''
	Return a list of test cases
	'''
	f = open(filename)
	numTests = int(f.readline())
	tests = [None] * numTests
	for k in range(numTests):
		board = [None] * N
		for i in range(N):
			board[i] = list(f.readline().strip())
		tests[k] = board
		f.readline()
	return tests

def writeOutput(filename, results):
	g = open(filename, 'w')
	for i in range(len(results)):
		g.write("Case #{}: {}\n".format(i+1, results[i]))
	g.close()

def checkRowWinner(row):
	if EMPTY in row:
		return NOTOVER
	elif T in row:
		if row.count(O) == N-1:
			return OWIN
		elif row.count(X) == N-1:
			return XWIN
		else:
			return DRAW
	else:
		if row.count(O) == N:
			return OWIN
		elif row.count(X) == N:
			return XWIN
		else:
			return DRAW

def checkWinner(board):
	def check(row):
		hasEmpty = False
		winner = None
		rowResult = checkRowWinner(row)
		if rowResult == NOTOVER:
			hasEmpty = True
		elif rowResult == XWIN:
			winner = XWIN
		elif rowResult == OWIN:
			winner = OWIN
		return (hasEmpty, winner)

	hasEmpty = False
		
	for i in range(N):
		row = board[i]
		(rowHasEmpty, winner) = check(row)
		if rowHasEmpty:
			hasEmpty = True
		if winner:
			return winner

	for j in range(N):
		column = [board[i][j] for i in range(N)]
		check(column)
		(rowHasEmpty, winner) = check(column)
		if rowHasEmpty:
			hasEmpty = True
		if winner:
			return winner

	
	diagonals = [ [board[k][k] for k in range(N)],
	              [board[k][N-k-1] for k in range(N)] ]
	for diag in diagonals:
		(rowHasEmpty, winner) = check(diag)
		if rowHasEmpty:
			hasEmpty = True
		if winner:
			return winner

	if hasEmpty:
		return NOTOVER
	else:
		return DRAW

def solveAll(testId):
	boards = readInput(testId + '.in')
	results = [checkWinner(board) for board in boards]
	writeOutput(testId + '.out', results)

def printBoard(board):
		for row in board:
			print row
		print

def printBoards(testId):
	tests = readInput(testId + '.in')
	for test in tests:
		printBoard(test)

class RowWinnerTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(XWIN, checkRowWinner([X,X,X,X]))

	def test2(self):
		self.assertEqual(OWIN, checkRowWinner([O,O,O,O]))

	def test3(self):
		self.assertEqual(XWIN, checkRowWinner([X,X,X,T]))

	def test4(self):
		self.assertEqual(OWIN, checkRowWinner([O,T,O,O]))

	def test5(self):
		self.assertEqual(DRAW, checkRowWinner([X,O,X,X]))

	def test6(self):
		self.assertEqual(DRAW, checkRowWinner([X,O,X,T]))

	def test7(self):
		self.assertEqual(NOTOVER, checkRowWinner([X,O,X,EMPTY]))

	def test8(self):
		self.assertEqual(NOTOVER, checkRowWinner([X,EMPTY,T,X]))

	def test9(self):
		self.assertEqual(NOTOVER, checkRowWinner([EMPTY, EMPTY, EMPTY, EMPTY]))


if __name__ == '__main__':
#	printBoards('sample')

#	suite = unittest.TestLoader().loadTestsFromTestCase(RowWinnerTest)
#	unittest.TextTestRunner(verbosity=2).run(suite)

#	solveAll('sample')
#	solveAll('A-small-attempt0')
	solveAll('A-large')

