o_player = 'O'
x_plater = 'X'
no_one = 'N'

def has_player_won(player, section):
	return all(p == player or p =='T' for p in section)

def check_rows(board):
	for row_idx in range(0,4):
		if has_player_won(x_plater, board[row_idx*4:row_idx*4 + 4]):
			return x_plater
		if has_player_won(o_player, board[row_idx*4:row_idx*4 + 4]):
			return o_player
	return 'N'

def check_columns(board):
	for col_idx in range(0,4):
		column = [p for idx,p in enumerate(board) if (idx%4==col_idx)]
		if has_player_won(x_plater, column):
			return x_plater
		if has_player_won(o_player, column):
			return o_player
	return no_one

def check_diagonal(board):
	lr_diagonal = [board[0], board[5], board[10], board[15]]
	rl_diagonal = [board[3], board[6], board[9], board[12]]
	if has_player_won(x_plater, lr_diagonal):
		return x_plater
	if has_player_won(o_player, lr_diagonal):
		return o_player
	if has_player_won(o_player, rl_diagonal):
		return o_player
	if has_player_won(x_plater, rl_diagonal):
		return x_plater
	return no_one

f = open('A-large.in', 'r')
out = open('output.txt', 'w')
tc_count = f.readline()
print tc_count
for tc_idx in range(0,int(tc_count)):
	board = []
	for row in range(0,4):
		board.extend(list(f.readline().strip()))
	f.readline()
	#print board
	player = check_rows(board)
	case_number = tc_idx + 1
	if player != no_one:
		out.write("Case #" + str(case_number) + ": " + player + " won\n")
		continue
	player = check_columns(board)
	if player != no_one:
		out.write("Case #" + str(case_number) + ": " + player + " won\n")
		continue
	player =  check_diagonal(board)
	if player != no_one:
		out.write("Case #" + str(case_number) + ": " + player + " won\n")
		continue
	if all(p != '.' for p in board):
		out.write("Case #" + str(case_number) + ": " + "Draw\n")
		continue
	out.write("Case #" + str(case_number) + ": " + "Game has not completed\n")

	