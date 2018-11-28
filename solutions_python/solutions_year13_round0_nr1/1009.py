lines = [
	[0,1,2,3],
	[4,5,6,7],
	[8,9,10,11],
	[12,13,14,15],
	[0,4,8,12],
	[1,5,9,13],
	[2,6,10,14],
	[3,7,11,15],
	[0,5,10,15],
	[3,6,9,12],
	]

def check_line(board,line):
	current = 'T'
	for square in line:
		if current != board[square]:
			if board[square] == '.':
				return 'E'
			if current == 'T':
				current = board[square]
			elif board[square] != 'T':
				return
	return current

def input_and_compute(case_number):
	# reads user input
	board = ""
	for i in range(5):
		board += raw_input()

	full = True
	for line in lines:
		result = check_line(board,line)
		if result == 'X' or result == 'O':
			print 'Case #%d: %s won' % (case_number, result)
			return
		elif result == 'E':
			full = False
	if full:
		print 'Case #%d: Draw' % case_number
	else:
		print 'Case #%d: Game has not completed' % case_number


for i in range(int(raw_input())):
	input_and_compute(i+1)