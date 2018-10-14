from itertools import product

def is_winner(row, column):
	for move in product('012', repeat=2):
		move = [ -1 if x == '2' else int(x) for x in move]

		
		temp_row = row
		temp_column = column
		
		if move == [0,0]:
			continue

		try:
			winner = True
			for i in range(3):
				temp_row+=move[0]
				temp_column+=move[1]
				if temp_row < 0 or temp_column < 0 or [temp_row, temp_column] == [0,0]:
					raise ValueError()
				if board[temp_row][temp_column] == board[row][column] or board[temp_row][temp_column] == 'T':
					pass
				else:
					winner = False
			if winner:
				return True
		except Exception:
			pass
	return False
	



def get_winner(rows):
	global board
	gamecompleted = True
	for row in rows:
		board.append(list(row))
		
	for row_number, row in enumerate(board):
		for tile_number, tile in enumerate(row):
			if tile == '.':
				gamecompleted = False
			elif is_winner(row_number, tile_number):
				if tile == 'X':
					return "X won"
				else:
					return "O won"
	if gamecompleted:
		return "Draw"
	else:
		return "Game has not completed"


board = []
cases = int(raw_input())

for case in range(cases):
	board = []
	lines = []
	for line in range(4):
		lines.append(raw_input())
	raw_input()

	print("Case #{}: {}".format(case+1, get_winner(lines)))