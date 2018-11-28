def read_line(line):
	board_line = []
	for ch in line:
		board_line.append(ch)

	return board_line

def read_board(board_str):
	board = []
	for line in board_str.splitlines():		
		board.append(read_line(line))

	return board

def get_char(target_char, actual_char):
	if target_char == actual_char:
		return target_char	
	elif actual_char == 'T':
		return target_char
	elif actual_char == '.':
		return None
	else:
		return actual_char

def check_horiz(board, pos):
	'''print "Checking horiz: " + str(pos),'''
	x = pos[0]
	y = pos[1]
	check_char = board[y][x]	
	if x >= 3:
		if check_char == get_char(check_char, board[y][x-1]) == get_char(check_char, board[y][x-2]) == get_char(check_char, board[y][x-3]):
			return check_char		

	if x + 3 < len(board[y]):
		if check_char == get_char(check_char, board[y][x+1]) == get_char(check_char, board[y][x+2]) == get_char(check_char, board[y][x+3]):
			return check_char

	return None

def check_vert(board, pos):
	'''print "Checking vert: " + str(pos),'''
	x = pos[0]
	y = pos[1]
	check_char = board[y][x]	
	if y >= 3:
		if check_char == get_char(check_char, board[y-1][x]) == get_char(check_char, board[y-2][x]) == get_char(check_char, board[y-3][x]):
			return check_char		

	if y + 3 < len(board[y]):
		if check_char == get_char(check_char, board[y+1][x]) == get_char(check_char, board[y+2][x]) == get_char(check_char, board[y+3][x]):
			return check_char		

	return None

def check_diag(board, pos):
	
	x = pos[0]
	y = pos[1]
	check_char = board[y][x]
	'''print "Checking diag: " + str(pos) + ", " + check_char,'''
	blen = len(board[x])
	if x + 3 < blen and y + 3 < blen:
		if check_char == get_char(check_char, board[y+1][x+1]) == get_char(check_char, board[y+2][x+2]) == get_char(check_char, board[y+3][x+3]):
			return check_char		

	if x >= 3 and y + 3 < blen:
		if check_char == get_char(check_char, board[y+1][x-1]) == get_char(check_char, board[y+2][x-2]) == get_char(check_char, board[y+3][x-3]):
			return check_char		

	if x + 3 < blen and y >= 3:
		if check_char == get_char(check_char, board[y-1][x+1]) == get_char(check_char, board[y-2][x+2]) == get_char(check_char, board[y-3][x+3]):
			return check_char		

	if x >= 3 and y >= 3:
		if check_char == get_char(check_char, board[y-1][x-1]) == get_char(check_char, board[y-2][x-2]) == get_char(check_char, board[y-3][x-3]):
			return check_char
	return None

def outcome(board):
	empty_chars = False
	for y in range(0, len(board)):
		for x in range(0, len(board[y])):
			if board[y][x] == '.':
				empty_chars = True
			else:
				winner = check_horiz(board, (x, y))
				if winner:
					return winner
				winner = check_vert(board, (x, y))
				if winner:
					return winner

				winner = check_diag(board, (x, y))
				if winner:
					return winner

	if empty_chars:
		return 'N'
	else:
		return 'D'

def process_input(input):	
	cases = []	
	buffer = ""
	for i in range(1, len(input)):
		line = input[i].strip()		
		if line == '':
			cases.append(buffer)
			buffer = ""
		else:			
			buffer = buffer + line + "\n"
	cases.append(buffer)
	
	return cases

def solve(input, output):
	cases = process_input(input)
	i = 1
	for case in cases:
		board = read_board(case)
		winner = outcome(board)
		case_outcome = "Case #" + str(i) + ": "
		if winner == 'N':
			case_outcome += "Game has not completed"
		elif winner == 'D':
			case_outcome += "Draw"
		elif winner:
			case_outcome += winner + " won"	
		i = i + 1
		output.write(case_outcome + "\n")
		print case_outcome

def main():
	import os, sys
	f = open(sys.argv[1])
	input = f.readlines()
	output = open(sys.argv[2], 'w')
	solve(input, output)

if __name__ == "__main__":
    main()