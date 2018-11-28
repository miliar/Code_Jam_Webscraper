import sys

t = input()

for test_case in range(t):

	game_ended = True

	
	board = []
	for i in range(4):
		line = raw_input()
		board_line = [l for l in line]
		board.append(board_line)
		if game_ended and '.' in board_line:
			game_ended = False

	if test_case < t-1:
		line = raw_input()

	game_veredict = ""

	last_row_check = ['.' for i in range(4)]
	last_col_check = ['.' for i in range(4)]
	last_main_diag_check = ['.']
	last_sec_diag_check = ['.']

	for i in range(4):
		for j in range(4):
			
			if i == 0 or last_col_check[j-1] == 'T':
				last_col_check[j] = board[i][j]
			else:
				if (last_col_check[j] == '.') or (board[i][j] != 'T' and board[i][j] != last_col_check[j]):
					last_col_check[j] = '.'


			if j == 0 or last_row_check[i-1] == 'T':
				last_row_check[i] = board[i][j]
			else:
				if (last_row_check[i] == '.') or (board[i][j] != 'T' and board[i][j] != last_row_check[i]):
					last_row_check[i] = '.'

			if i == j:
				if (i == 0 and j == 0) or last_main_diag_check[0] == 'T':
					last_main_diag_check[0] = board[i][j]
					# print "switch " + last_main_diag_check[0] + " for " + board[i][j]
				else:
					if (last_main_diag_check[0] == '.') or (board[i][j] != 'T' and board[i][j] != last_main_diag_check[0]):
						last_main_diag_check[0] = '.'
						# print "switch " + last_main_diag_check[0] + " for " + board[i][j]

			if i == 3-j:
				if (i == 0 and j == 3) or last_sec_diag_check[0] == 'T':
					last_sec_diag_check[0] = board[i][j]
				else:
					if (last_sec_diag_check[0] == '.') or (board[i][j] != 'T' and board[i][j] != last_sec_diag_check[0]):
						last_sec_diag_check[0] = '.'
				

	winner = ''
	

	# print last_row_check
	# print last_col_check
	# print last_main_diag_check
	# print last_sec_diag_check
	
	for i in range(4):
		if last_row_check[i] != '.':
			winner = last_row_check[i]
			# print "win by row"
			break
		if last_col_check[i] != '.':
			winner = last_col_check[i]
			# print "win by col"
			break
	if winner == '':
		if last_main_diag_check[0] != '.':
			winner = last_main_diag_check[0]
			# print "win by main diag"

	if winner == '':
		if last_sec_diag_check[0] != '.':
			winner = last_sec_diag_check[0]
			# print "win by sec diag"

	if winner != '':
		game_veredict = winner + " won"

	if game_ended and game_veredict == "":
		game_veredict = "Draw"

	if not game_ended and game_veredict == "":
		game_veredict = "Game has not completed"

	print "Case #" + str(test_case + 1) + ": " + game_veredict