WIN = 1
HAS_SPACE = 2
NO_SPACE = 3

def checkColumn(arr, row, unExpectedChars):
	result = True
	hasSpace = False
	for col in range(4):
		if arr[row][col] in unExpectedChars:
			result = False
		if arr[row][col] == '.':
			hasSpace = True
	return (result, hasSpace)

def checkRow(arr, col, unExpectedChars):
	result = True
	hasSpace = False
	for row in range(4):
		if arr[row][col] in unExpectedChars:
			result = False
		if arr[row][col] == '.' :
			hasSpace = True
	return (result, hasSpace)

def checkMainDiagonal(arr, unExpectedChars):
	result = True

	for row in range(4):
		if arr[row][row] in unExpectedChars:
			result = False
			break
	return result	

def checkOtherDiagonal(arr, unExpectedChars):
	result = True

	for row in range(4):
		if arr[row][3 - row] in unExpectedChars:
			result = False
			break
	return result	


ntests = int(raw_input())

for i in range(ntests) :
	line1 = raw_input()
	line2 = raw_input()
	line3 = raw_input()
	line4 = raw_input()
	try :
		raw_input()
	except:
		pass

	arr = [[c for c in line1], [c for c in line2], [c for c in line3], [c for c in line4]]

	hasSpace = False
	globalXwin = False
	globalOwin = False

	for row in range(4):
		(localXwin, localSpace) = checkColumn(arr, row, ['O', '.'])
		if localXwin :
			globalXwin = True
		if localSpace :
			hasSpace = True

		(localOwin, localSpace) = checkColumn(arr, row, ['X', '.'])
		if localOwin :
			globalOwin = True
		if localSpace :
			hasSpace = True

	for col in range(4):
		(localXwin, localSpace) = checkRow(arr, col, ['O', '.'])
		if localXwin :
			globalXwin = True

		(localOwin, localSpace) = checkRow(arr, col, ['X', '.'])
		if localOwin :
			globalOwin = True

	localOwin = checkMainDiagonal(arr, ['X', '.'])
	if localOwin :
		globalOwin = True
	localOwin = checkOtherDiagonal(arr, ['X', '.'])
	if localOwin :
		globalOwin = True

	localXwin = checkMainDiagonal(arr, ['O', '.'])
	if localXwin :
		globalXwin = True
	localXwin = checkOtherDiagonal(arr, ['O', '.'])
	if localXwin :
		globalXwin = True

	resultstr = "Case #" + str(i+1) + ": "
	if globalXwin:
		resultstr += "X won"
	elif globalOwin:
		resultstr += "O won"
	elif hasSpace:
		resultstr += "Game has not completed"
	else:
		resultstr += "Draw"
	print resultstr