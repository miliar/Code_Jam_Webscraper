#!/usr/bin/python


import sys

if len(sys.argv) != 2:
    print "Please run program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File could not be opened"
    sys.exit()

case = 1

while count > 0:
	complete = True
	count = count - 1
	Matrix = [[0 for x in xrange(4)] for x in xrange(4)]

	line = f.readline() # XXXT
	if not line:
		break

	if '.' in line:
		complete = False
	Matrix[0][0] = line[0]
	Matrix[0][1] = line[1]
	Matrix[0][2] = line[2]
	Matrix[0][3] = line[3]

	line = f.readline() # XXXT
	if not line:
		break

	if '.' in line:
		complete = False

	Matrix[1][0] = line[0]
	Matrix[1][1] = line[1]
	Matrix[1][2] = line[2]
	Matrix[1][3] = line[3]

	line = f.readline() # XXXT
	if not line:
		break

	if '.' in line:
		complete = False

	Matrix[2][0] = line[0]
	Matrix[2][1] = line[1]
	Matrix[2][2] = line[2]
	Matrix[2][3] = line[3]

	line = f.readline() # XXXT
	if not line:
		break
	if '.' in line:
		complete = False

	Matrix[3][0] = line[0]
	Matrix[3][1] = line[1]
	Matrix[3][2] = line[2]
	Matrix[3][3] = line[3]

	#print Matrix

	# check Rows
	draw = False
	winner = '.'
	row_i = 0
	while row_i < 4:

		test = False
		test = (Matrix[row_i][0] == Matrix[row_i][1] and 
			Matrix[row_i][1] == Matrix[row_i][2] and 
			Matrix[row_i][2] == Matrix[row_i][3] and Matrix[row_i][0] != '.')

		test = test or (Matrix[row_i][0] == 'T' and 
			Matrix[row_i][1] == Matrix[row_i][2] and 
			Matrix[row_i][2] == Matrix[row_i][3] and Matrix[row_i][3] != '.')

		test = test or (Matrix[row_i][0] == Matrix[row_i][2] and 
			Matrix[row_i][1] == 'T' and 
			Matrix[row_i][2] == Matrix[row_i][3] and Matrix[row_i][0] != '.')

		test = test or (Matrix[row_i][0] == Matrix[row_i][1] and 
			Matrix[row_i][2] == 'T' and 
			Matrix[row_i][1] == Matrix[row_i][3] and Matrix[row_i][3] != '.')

		test = test or (Matrix[row_i][0] == Matrix[row_i][1] and 
			Matrix[row_i][1] == Matrix[row_i][2] and 
			Matrix[row_i][3] == 'T' and Matrix[row_i][2] != '.')

		if test:

			if winner == '.':
				if Matrix[row_i][0] != 'T':
					winner = Matrix[row_i][0]
				else:
					winner = Matrix[row_i][3]
			else:
				if Matrix[row_i][0] != 'T':
					temp = Matrix[row_i][0]
				else:
					temp = Matrix[row_i][3]
				if temp != winner:
					draw = True
					break
			#print "Row " + winner		
		row_i = row_i + 1


	# check columns
	if not draw:
		col_i = 0
		while col_i < 4:

			test = False
			test = (Matrix[0][col_i] == Matrix[1][col_i] and 
				Matrix[1][col_i] == Matrix[2][col_i] and 
				Matrix[2][col_i] == Matrix[3][col_i] and Matrix[0][col_i] != '.') 
			test = test	or (Matrix[0][col_i] == 'T' and 
				Matrix[1][col_i] == Matrix[2][col_i] and 
				Matrix[2][col_i] == Matrix[3][col_i] and Matrix[1][col_i] != '.')
			test = test	or (Matrix[0][col_i] == Matrix[2][col_i] and 
				Matrix[1][col_i] == 'T' and 
				Matrix[2][col_i] == Matrix[3][col_i] and Matrix[0][col_i] != '.')
			test = test	or (Matrix[0][col_i] == Matrix[1][col_i] and 
				Matrix[2][col_i] == 'T' and 
				Matrix[1][col_i] == Matrix[3][col_i] and Matrix[0][col_i] != '.')
			test = test	or (Matrix[0][col_i] == Matrix[1][col_i] and 
				Matrix[1][col_i] == Matrix[2][col_i] and 
				Matrix[3][col_i] == 'T' and Matrix[0][col_i] != '.')

			if test:

				if winner == '.':
					if Matrix[0][col_i] != 'T':
						winner = Matrix[0][col_i]
					else:
						winner = Matrix[3][col_i]
				else:
					if Matrix[0][col_i] != 'T':
						temp = Matrix[0][col_i]
					else:
						temp = Matrix[3][col_i]
					if temp != winner:
						draw = True
						break
				#print "Column " + winner
			col_i = col_i + 1


		# check daigonals
		if not draw:
			test = False
			test = (Matrix[0][0] == Matrix[1][1] and 
				Matrix[1][1] == Matrix[2][2] and 
				Matrix[2][2] == Matrix[3][3] and Matrix[0][0] != '.')

			test = test or (Matrix[0][0] == 'T' and 
				Matrix[1][1] == Matrix[2][2] and 
				Matrix[2][2] == Matrix[3][3] and Matrix[1][1] != '.')

			test = test or (Matrix[0][0] == Matrix[2][2] and 
				Matrix[1][1] == 'T' and 
				Matrix[2][2] == Matrix[3][3] and Matrix[0][0] != '.')
			test = test or (Matrix[0][0] == Matrix[1][1] and 
				Matrix[2][2] == 'T' and 
				Matrix[1][1] == Matrix[3][3] and Matrix[0][0] != '.')
			test = test or (Matrix[0][0] == Matrix[1][1] and 
				Matrix[1][1] == Matrix[2][2] and 
				Matrix[3][3] == 'T' and Matrix[0][0] != '.')

			if test:
				if winner == '.':
					if Matrix[0][0] != 'T':
						winner = Matrix[0][0]
					else:
						winner = Matrix[3][3]
				else:
					if Matrix[0][0] != 'T':
						temp = Matrix[0][0]
					else:
						temp = Matrix[3][3]
					if temp != winner:
						draw = True

				#print "Doagonal 1 " + winner

			if not draw:
				test = False
				test = (Matrix[0][3] == Matrix[1][2] and 
					Matrix[1][2] == Matrix[2][1] and 
					Matrix[2][1] == Matrix[3][0] and Matrix[0][3] != '.')

				test = test or (Matrix[0][3] == 'T' and 
					Matrix[1][2] == Matrix[2][1] and 
					Matrix[2][1] == Matrix[3][0]  and Matrix[2][1] != '.')

				test = test or (Matrix[0][3] == Matrix[2][1] and 
					Matrix[1][2] == 'T' and 
					Matrix[2][1] == Matrix[3][0]  and Matrix[0][3] != '.')
				test = test or (Matrix[0][3] == Matrix[1][2] and 
					Matrix[2][1] == 'T' and 
					Matrix[1][2] == Matrix[3][0]  and Matrix[0][3] != '.')
				test = test or (Matrix[0][3] == Matrix[1][2] and 
					Matrix[1][2] == Matrix[2][1] and 
					Matrix[3][0] == 'T'  and Matrix[0][3] != '.')

				if test:
					if winner == '.':
						if Matrix[0][3] != 'T':
							winner = Matrix[0][3]
						else:
							winner = Matrix[3][0]
					else:
						if Matrix[0][3] != 'T':
							temp = Matrix[0][3]
						else:
							temp = Matrix[3][0]
						if temp != winner:
							draw = True
					#print "Doagonal 2 " + winner

		if winner == "X":
			answer = "X won"
		if winner == "O":
			answer = "O won"
		elif winner!= 'X' and winner != 'O':
			if not complete:
				answer = "Game has not completed"
			elif draw or complete:
				answer = "Draw"

		print "Case #" + str(case) + ": " + answer
		case = case + 1
	#empty line
   	line = f.readline()
   	if not line:
   		break



