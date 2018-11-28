import math

input_file = open('A-large.in')

countlines = 0
caseNum = 1
array = []
phrases = ['Game has not completed', 'X won', 'O won', 'Draw']
for line in input_file:
	case = 0 #Game is not completed, 1: X Win, 2: O Win, 3: Draw 
	if countlines == 0:
		countlines+=1
	elif countlines % 5 == 0:
		countlines += 1
		array = []
		caseNum +=1
	elif countlines % 5 != 4:
		array.append(line[0:4])
		countlines+=1
	else:
		array.append(line[0:4])
		if '.' not in array[0] and '.' not in array[1] and '.' not in array[2] and '.' not in array[3]:
			case = 3
		for row in array:
			if row == "XXXX" or row == "XXXT" or row == "XXTX" or row == "XTXX" or row == "TXXX":
				case = 1
			elif row == "OOOO" or row == "OOOT" or row == "OOTO" or row == "OTOO" or row == "TOOO":
				case = 2
		for i in xrange(4):
			if (array[0][i] == "X" or array[0][i] == "T") and (array[1][i] == "X" or array[1][i] == "T") and (array[2][i] == "X" or array[2][i] == "T") and (array[3][i] == "X" or array[3][i] == "T"):
				case = 1
			if (array[0][i] == "O" or array[0][i] == "T") and (array[1][i] == "O" or array[1][i] == "T") and (array[2][i] == "O" or array[2][i] == "T") and (array[3][i] == "O" or array[3][i] == "T"):
				case = 2
		if (array[0][0] == "X" or array[0][0] == "T") and (array[1][1] == "X" or array[1][1] == "T") and (array[2][2] == "X" or array[2][2] == "T") and (array[3][3] == "X" or array[3][3] == "T"):
			case = 1
		if (array[0][0] == "O" or array[0][0] == "T") and (array[1][1] == "O" or array[1][1] == "T") and (array[2][2] == "O" or array[2][2] == "T") and (array[3][3] == "O" or array[3][3] == "T"):
			case = 2
		if (array[0][3] == "X" or array[0][3] == "T") and (array[1][2] == "X" or array[1][2] == "T") and (array[2][1] == "X" or array[2][1] == "T") and (array[3][0] == "X" or array[3][0] == "T"):
			case = 1
		if (array[0][3] == "O" or array[0][3] == "T") and (array[1][2] == "O" or array[1][2] == "T") and (array[2][1] == "O" or array[2][1] == "T") and (array[3][0] == "O" or array[3][0] == "T"):
			case = 2
		countlines+=1
		print 'Case #' + str(caseNum) + ': ' + phrases[case]



