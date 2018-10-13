from sys import argv

script, input_file = argv
	

def check_diagonal(board, t_loc):
	result = -1
	t_on_diag_left = (t_loc[0] == t_loc[1])
	t_on_diag_right = t_loc[0] + t_loc[1] == 3
	if  (not t_on_diag_left) and (board[0][0] == board[1][1] and board[2][2] == board[3][3] and board[0][0] == board[2][2]) and board[0][0] != '.':
		result = board[0][0]
	
	elif (not t_on_diag_left) and (board[0][3] == board[1][2] and board[2][1] == board[3][0] and board[1][2] == board[2][1]) and board[0][3] != '.':
		result = board[0][3]
	
	elif t_on_diag_left and board[0][0] != '.' and board[1][1] != '.' and board[2][2] != '.' and board[3][3] != '.':
		row = 0
		count = 0
		player = board[0][0]
		if player == 'T':
			player = board[1][1]
		for i in board:
			if row != t_loc[0] and i[row] == player:
				count = count + 1
			row = row + 1
		if count == 3:
			result = player
	
	elif t_on_diag_right and board[0][3] != '.' and board[1][2] != '.' and board[2][1] != '.' and board[3][0] != '.':
		row = 0
		count = 0
		player = board[0][3]
		if player == 'T':
			player = board[2][1]
		for i in board:
			if row != t_loc[0] and i[3 - row] == player:
				count = count + 1
			row = row + 1
		if count == 3:
			result = player
	return result

def check_horizontal(board):
	result = -1
	for i in board:
		print "i = ", i
		if i == "XXXX\n" or i =="TXXX\n" or i =="XTXX\n" or i == "XXTX\n" or i == "XXXT\n":
			result = 'X'
		elif i == "OOOO" or i =="TOOO" or i =="OTOO" or i == "OOTO" or i == "OOOT":
			result = 'O'
	return result

def check_vertical(board, t_loc):
	result = -1
	i = 0
	while i < 4:
		if board[0][i] == board[1][i] and board[2][i] == board[3][i] and board[0][i] == board[2][i] and board[0][i] != '.' and i != t_loc[1]:
			result = board[0][i]
		elif i == t_loc[1]:
			j = 0
			count = 0
			player = board[0][i]
			if t_loc[0] == 0:
				player = board[1][i]
			while j < 4:
				if board[j][i] == player and player != '.':
					count = count + 1
				j = j + 1
			if count == 3:
				result = player
		i = i + 1
	return result
		
		

def check_draw(board):
	result = "draw"
	for i in board:
		if '.' in i:
			result = -1
	return result
			

def check_win(board, t_loc):
	win = -1
	win = check_horizontal(board)
	if win == -1:
		win = check_vertical(board, t_loc)
		if win == -1:
			win = check_diagonal(board, t_loc)
	return win
def assess_board(board, t_loc):
	result = -1
	winner = check_win(board, t_loc)
	if winner != -1:
		result = winner
	else:
		result = check_draw(board)
	return result

	

def find_t(board):
	row = 0
	column  = -1
	result = [-1, -2]
	for i in board:
		if 'T' in i:
			column = i.index('T')
			result = [row, column]
		row = row + 1
	return result
			

def write_result(result, case_num):
	output = open('output.txt', 'a')
	print "case_num =  ", case_num
	print "result = ", result
	if result == 'X' or  result == 'O':
		output.write("Case #%s:  %c won\n" % (case_num, result))
	elif result == "draw":
		output.write("Case #%s:  Draw\n" % case_num)
	else:
		output.write("Case #%s:  Game has not completed\n" % case_num)
	
	
script, input_file = argv

input_data = open(input_file)

num_cases = int(input_data.readline())
i = 0

board = []
while i < num_cases:
	board.append(input_data.readline())
	board.append(input_data.readline())
	board.append(input_data.readline())
	board.append(input_data.readline())
	t_loc = find_t(board)
	blank = input_data.readline()
	result = assess_board(board, t_loc)
	output = write_result(result, i + 1)
	i = i + 1
	board = []

	