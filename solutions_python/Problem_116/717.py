ROWS = 4
COLUMNS = 4
input_file = open('A-Large.in', 'r')
output_file = open('A-Large.txt', 'w+')
line = input_file.readline()
num_cases = int(line)
for case_num in range(1,num_cases+1):
	board_finished = True
	board = [['' for i in range(ROWS)] for j in range(COLUMNS)]
	#read 4 lines into array
	for row in range(ROWS):
		line = input_file.readline()
		for column in range(COLUMNS):
			if board_finished and line[column] == '.':
				board_finished = False
			board[row][column] = line[column]

	winner = False
	#test every row
	for row in range(ROWS):
		num_Os = 0
		num_Xs = 0
		for column in range(COLUMNS):
			if board[row][column] == '.':
				#short-circuit
				break
			elif board[row][column] == 'T':
				num_Os += 1
				num_Xs += 1
			elif board[row][column] == 'O':
				num_Os += 1
			elif board[row][column] == 'X':
				num_Xs += 1
		if num_Os == 4:
			winner = 'O'
		elif num_Xs == 4:
			winner = 'X'

	#test every column
	for column in range(COLUMNS):
		num_Os = 0
		num_Xs = 0
		for row in range(ROWS):
			if board[row][column] == '.':
				#short-circuit
				break
			elif board[row][column] == 'T':
				num_Os += 1
				num_Xs += 1
			elif board[row][column] == 'O':
				num_Os += 1
			elif board[row][column] == 'X':
				num_Xs += 1
		if num_Os == 4:
			winner = 'O'
		elif num_Xs == 4:
			winner = 'X'	

	#forward diagonals
	num_Os = 0
	num_Xs = 0
	for index in range(ROWS):
		row = index
		column = index
		if board[row][column] == '.':
			#short-circuit
			break
		elif board[row][column] == 'T':
			num_Os += 1
			num_Xs += 1
		elif board[row][column] == 'O':
			num_Os += 1
		elif board[row][column] == 'X':
			num_Xs += 1
	if num_Os == 4:
		winner = 'O'
	elif num_Xs == 4:
		winner = 'X'

	#back diagonal
	num_Os = 0
	num_Xs = 0
	for index in range(ROWS):
		row = index
		column = 3-index
		if board[row][column] == '.':
			#short-circuit
			break
		elif board[row][column] == 'T':
			num_Os += 1
			num_Xs += 1
		elif board[row][column] == 'O':
			num_Os += 1
		elif board[row][column] == 'X':
			num_Xs += 1
	if num_Os == 4:
		winner = 'O'
	elif num_Xs == 4:
		winner = 'X'

	#print result
	if winner:
		result = winner+' won'
	else:
		if board_finished:
			result = 'Draw'
		else:
			result = 'Game has not completed'
	output_file.write('Case #'+str(case_num)+': '+result+'\n')
	#read empty line
	input_file.readline()


