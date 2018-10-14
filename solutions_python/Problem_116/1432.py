#!/usr/bin/python3

def read_input(filename):
	lines = open(filename, 'r').read().splitlines()
	number_of_inputs = lines[0]
	assert int(number_of_inputs) == (len(lines))//5
	boardlist = []
	for i in range(1, len(lines), 5):
		board_input = lines[i:i+5]
		boardlist.append(board_input)
	return boardlist

def parse_input(boardlist):
	boards = []
	for board_input in boardlist:
		board = [[0 for x in range(4)] for y in range(4)]
		has_empty = False
		for row in range(4):
			if "." in board_input[row]:
				has_empty = True
			for col in range(4):
				board[row][col] = board_input[row][col]
		boards.append((not has_empty,board))
	return boards

def check_game(game):
	(full, board) = game
	winner = False
	winner = check_rows(board) or check_cols(board) or check_diags(board)
	return (full or winner, winner)

def check_line(line):
	if '.' in line:
		return False
	if 'X' in line and 'O' in line:
		return False
	if 'X' in line:
		return 'X'
	if 'O' in line:
		return 'O'
	raise Exception("Invalid input!")

def check_rows(board):
	winner = False
	for row in board:
		res = check_line(row)
		if res:
			winner = res
			break
	return winner

def check_cols(board):
	winner = False
	for col in range(4):
		column = [board[x][col] for x in range(4)]
		res = check_line(column)
		if res:
			winner = res
			break
	return winner

def check_diags(board):
	diag1 = [board[x][x] for x in range(4)]
	diag2 = [board[x][3-x] for x in range(4)]
	
	return check_line(diag1) or check_line(diag2)

def main():
	input = read_input("input.txt")
	games = parse_input(input)
	cnt = 0
	for game in games:
		cnt += 1
		print("Case #", cnt, ":", sep="", end=" ")
		(ended, who) = check_game(game)
		if ended:
			if who:
				print(who, "won")
			else:
				print("Draw")
		else:
			print("Game has not completed")

if __name__ == "__main__":
	main()
