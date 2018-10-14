num_cases = int(raw_input())
for case in range(1,num_cases+1):
	print "Case #"+str(case)+":",
	matrix = []
	for i in range(0, 4):
		line = raw_input()
		matrix.append(list(line))

	oWonDiag1 = 1
	oWonDiag2 = 1
	xWonDiag1 = 1
	xWonDiag2 = 1
	empty = 0
	for i in range(0, 4):
		oWonLines = 1
		oWonColumns = 1
		xWonLines = 1
		xWonColumns = 1
		for j in range(0,4):
			if (matrix[i][j] == '.'):
				empty = 1			
			if (matrix[i][j] != 'O' and matrix[i][j] != 'T'):
				oWonLines = 0
			if (matrix[j][i] != 'O' and matrix[j][i] != 'T'):
				oWonColumns = 0
			if (matrix[i][j] != 'X' and matrix[i][j] != 'T'):
				xWonLines = 0
			if (matrix[j][i] != 'X' and matrix[j][i] != 'T'):
				xWonColumns = 0
		if (oWonLines or oWonColumns or xWonLines or xWonColumns):
			oWonDiag1 = 0
			oWonDiag2 = 0
			xWonDiag1 = 0
			xWonDiag2 = 0
			break
		if (matrix[i][i] != 'O' and matrix[i][i] != 'T'):
			oWonDiag1 = 0
		if (matrix[i][3-i] != 'O' and matrix[i][3-i] != 'T'):
			oWonDiag2 = 0
		if (matrix[i][i] != 'X' and matrix[i][i] != 'T'):
			xWonDiag1 = 0
		if (matrix[i][3-i] != 'X' and matrix[i][3-i] != 'T'):
			xWonDiag2 = 0
	#print oWonLines , oWonColumns , oWonDiag1 , oWonDiag2
	if (oWonLines or oWonColumns or oWonDiag1 or oWonDiag2):
		print "O won"
	elif (xWonLines or xWonColumns or xWonDiag1 or xWonDiag2):
		print "X won"
	elif (empty):
		print "Game has not completed"
	else:
		print "Draw"

	raw_input()




