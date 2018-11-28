import sys

num = int(sys.stdin.readline());

lines = [s.strip() for s in sys.stdin.readlines()]

board = []

def orMap2_Columns(board, fun):
	for x in range(0,4):
		atLeastOne = False
		for y in range(0,4):
			if not fun(board[y][x]):
				atLeastOne = True
				break
		if not atLeastOne: return True
	return False

def orMap2_Rows(board, fun):
	for y in range(0,4):
		atLeastOne = False
		for x in range(0,4):
			if not fun(board[y][x]):
				atLeastOne = True
				break
		if not atLeastOne: return True
	return False

def orMap2_Diag(board, fun):
	for yfun in [lambda x: x, lambda x: 3-x]:
		atLeastOne = False
		for x in range(0,4):
			y = yfun(x)
			if not fun(board[y][x]):
				atLeastOne = True
				break
		if not atLeastOne: return True
	return False

def anyMap2(board, fun):
	return orMap2_Columns(board, fun) or orMap2_Rows(board, fun) or orMap2_Diag(board, fun)

def andMap(board, fun):
	for y in range(0,4):
		for x in range(0,4):
			if not fun(board[y][x]):
				return False
	return True

caseNum = 1;
for line in lines:
	if line == '':
		print('Case #' + str(caseNum) + ': ', end='')

		# compute and print board state
		if anyMap2(board, lambda cell: cell == 'X' or cell == 'T'):
			print('X won')
		elif anyMap2(board, lambda cell: cell == 'O' or cell == 'T'):
			print('O won')
		elif andMap(board, lambda cell: cell != '.'):
			print('Draw')
		else:
			print('Game has not completed')
		# update variables
		caseNum += 1
		board = []
	else:
		board.append(line)