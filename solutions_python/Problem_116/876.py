f = open('tictac.in');
out = open('tictac.out', 'w')
cases = int(f.readline())

def getResult(board):
	# rows
	for i in range(4):
		line = board[i]
		result = winning_line(line)
		if result != False:
			return result

	#cols
	for i in range(4):
		line = [board[j][i] for j in range(4)]
		result = winning_line(line)
		if result != False:
			return result

	#diagonals
	line = [board[i][i] for i in range(4)]
	result = winning_line(line)
	if result != False:
		return result

	line2 = [board[i][3-i] for i in range(4)]
	result = winning_line(line2)
	if result != False:
		return result

def winning_line(line):
	if line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
		return "X won"
	elif line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
		return "O won"
	else:
		return False

def draw(board):
	for i in range(4):
		for j in range(4):
			if board[i][j] == '.':
				return False
	return True;

for case in range(1, cases+1):
	board = [];
	for _ in range(4):
		board.append(f.readline())

	result =  getResult(board)
	if result is None:
		if draw(board):
			out.write("Case #" + str(case) + ": Draw\n")
		else:
			out.write("Case #" + str(case) + ": Game has not completed\n")
	else:
		out.write("Case #" + str(case) + ": " + result + "\n")
	f.readline()
	# out.write('asdf')

