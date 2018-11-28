def main():
	with open("A-large.in", "r") as f:
		num_test_cases = int(f.readline())

		for test_case_index in range(num_test_cases):
			board = []
			for row_index in range(4):
				line = f.readline()
				row = []
				for i in range(4):
					row.append(line[i])
				board.append(row)

			f.readline()
			board_status = get_board_status(board)
			print "Case #" + str(test_case_index + 1) + ": " + board_status
		

def get_board_status(board):
	board_has_empty_square = False
	lines_to_check = []
	# Check all rows
	for i in range(4):
		lines_to_check.append(board[i])

	# Check all columns
	for i in range(4):
		column = [row[i] for row in board]
		lines_to_check.append(column)

	# Check all diagonal
	lines_to_check.append([board[i][i] for i in range(4)])
	lines_to_check.append([board[i][3-i] for i in range(4)])

	for line in lines_to_check:
		winner, line_has_empty_square = get_line_status(line)
		board_has_empty_square = board_has_empty_square or line_has_empty_square
		if winner:
			return winner + " won"

	if board_has_empty_square:
		return "Game has not completed"
	else:
		return "Draw"
	

def get_line_status(line):
	has_winner = True
	winner = None
	has_empty_square = False
	for i in range(4):
		if line[i] == ".":
			has_winner = False
			has_empty_square = True
		elif line[i] != "T":
			if winner is None:
				winner = line[i]
			elif winner != line[i]:
				has_winner = False

	if has_winner:
		return winner, has_empty_square
	else:
		return None, has_empty_square


if __name__ == "__main__":
	main()
