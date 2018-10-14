def horizontal():
	for k in range(0, 4):
		xPossible = True
		oPossible = True
		for j in range(0, 4):
			if board[k][j] == '.':
				oPossible = False
				xPossible = False
				global notFinishedYet
				notFinishedYet = True
			elif board[k][j] == 'X':
				oPossible = False
			elif board[k][j] == 'O':
				xPossible = False
			if not xPossible and not oPossible:
				break
		if xPossible:
			print 'Case #'+`i+1`+': X won'
			return True
		if oPossible:
			print 'Case #'+`i+1`+': O won'
			return True
	return False

def vertical():
	for k in range(0, 4):
		xPossible = True
		oPossible = True
		for j in range(0, 4):
			if board[j][k] == '.':
				oPossible = False
				xPossible = False
			elif board[j][k] == 'X':
				oPossible = False
			elif board[j][k] == 'O':
				xPossible = False
			if not xPossible and not oPossible:
				break
		if xPossible:
			print 'Case #'+`i+1`+': X won'
			return True
		if oPossible:
			print 'Case #'+`i+1`+': O won'
			return True
	return False

def slash():
	xPossible = True
	oPossible = True
	for (j, k) in [(0, 3),(1, 2), (2, 1), (3, 0)]:
		if board[j][k] == '.':
			oPossible = False
			xPossible = False
		elif board[j][k] == 'X':
			oPossible = False
		elif board[j][k] == 'O':
			xPossible = False
		if not xPossible and not oPossible:
			break
	if xPossible:
		print 'Case #'+`i+1`+': X won'
		return True
	if oPossible:
		print 'Case #'+`i+1`+': O won'
		return True
	return False

def backSlash():
	xPossible = True
	oPossible = True
	for (j, k) in [(0, 0),(1, 1), (2, 2), (3, 3)]:
		if board[j][k] == '.':
			oPossible = False
			xPossible = False
		elif board[j][k] == 'X':
			oPossible = False
		elif board[j][k] == 'O':
			xPossible = False
		if not xPossible and not oPossible:
			break
	if xPossible:
		print 'Case #'+`i+1`+': X won'
		return True
	if oPossible:
		print 'Case #'+`i+1`+': O won'
		return True
	return False

t = input()
for i in range(0, t):
	board = []
	for j in range(0, 4):
		board.append(raw_input())
	raw_input()
	notFinishedYet = False
	if not horizontal() and not vertical() and not slash() and not backSlash():
		if notFinishedYet:
			print 'Case #'+`i+1`+': Game has not completed'
		else:
			print 'Case #'+`i+1`+': Draw'