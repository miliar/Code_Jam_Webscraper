import sys

file = sys.stdin

n = int(file.readline())

def readboard(file):
	board = dict()
	for i in range(0,4):
		line = file.readline()
		"print line"
		for j in range(0,4):
			board[(i,j)] = line[j]
	return board

def procboard(board):
	
	"Check X victory"
	xcol = [0] * 4
	xrow = [0] * 4
	xd1 = 0
	xd2 = 0
	ocol = [0] * 4
	orow = [0] * 4
	od1 = 0
	od2 = 0
	completed = 'D'
	for i in range(0,4):
		for j in range(0,4):
			cell = board[(i,j)]
			"print cell"
			if cell == 'X' or cell == 'T':
				xrow[i] += 1
				xcol[j] += 1
				if i == j:
					xd1 += 1
				if i + j == 3:
					xd2 += 1
			if cell == 'O' or cell == 'T':
				orow[i] += 1
				ocol[j] += 1
				if i == j:
					od1 += 1
				if i + j == 3:
					od2 += 1
			if cell == '.':
				completed = '.'
	for i in range(0,4):
		if xrow[i] == 4 or xcol[i] == 4 or xd1 == 4 or xd2 == 4:
			return 'X'
		elif orow[i] == 4 or ocol[i] == 4 or od1 == 4 or od2 == 4:
			return 'O'
	return completed

for k in range(1,n+1):
	board = readboard(file)
	res = procboard(board)
	out = "error"
	if res == 'X':
		out = "Case #{0}: X won"
	elif res == 'O':
		out = "Case #{0}: O won"
	elif res == 'D':
		out = "Case #{0}: Draw"
	elif res == '.':
		out = "Case #{0}: Game has not completed"
	print out.format(k)
	file.readline()
