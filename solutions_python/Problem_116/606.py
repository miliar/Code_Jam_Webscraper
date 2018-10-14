def load_board():
	board = ''
	for i in range(0, 4):
		board += raw_input()
	raw_input()
	return board

def check_line(board, line):
	count = {'X':0, 'O':0, '.':0, 'T':0}
	for position in line:
		count[board[position]] += 1
	if count['X'] + count['T'] == 4:
		return 'X won'
	elif count['O'] + count['T'] == 4:
		return 'O won'
	else:
		return None

def check_end_game(board):
	if board.find('.') == -1:
		return 'Draw'
	else:
		return 'Game has not completed'

def solve_board(board, lines):
	for line in lines:
		result = check_line(board, line)
		if result:
			return result
	result = check_end_game(board)
	if result:
		return result
	# should not reach here
	return 'Invalid board state.'


lines = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15], [0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15], [0,5,10,15], [3,6,9,12]]
n = int(raw_input())
for i in range(0, n):
  board = load_board()
  result = solve_board(board, lines)
  print 'Case #%s: %s' % (i+1, result)