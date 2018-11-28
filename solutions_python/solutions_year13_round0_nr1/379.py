def hasLine(squares, symbol):
	for i in range(4):
		if squares[i][0] == squares[i][1] == squares[i][2] == squares[i][3] == symbol:
			return True
	for i in range(4):
		if squares[0][i] == squares[1][i] == squares[2][i] == squares[3][i] == symbol:
			return True
	if squares[0][0] == squares[1][1] == squares[2][2] == squares[3][3] == symbol:
		return True
	if squares[0][3] == squares[1][2] == squares[2][1] == squares[3][0] == symbol:
		return True
	return False

def hasEmpty(squares):
	for i in range(4):
		for j in range(4):
			if squares[i][j] == '.':
				return True
	return False

file = open("A-large.in")
n = int(file.readline())
for case in range(n):
	squares = [list(file.readline()) for i in range(4)]
	file.readline()
	print("Case #{:d}:".format(case+1)),
	Tpos = None
	for i in range(4):
		if 'T' in squares[i]:
			index = squares[i].index('T')
			Tpos = (i, index)
			break
	if Tpos != None:
		squares[Tpos[0]][Tpos[1]] = 'X'
	if hasLine(squares, 'X'):
		print("X won")
	else:
		if Tpos != None:
			squares[Tpos[0]][Tpos[1]] = 'O'
		if hasLine(squares, 'O'):
			print("O won")
		else:
			if hasEmpty(squares):
				print("Game has not completed")
			else:
				print("Draw")
file.close()