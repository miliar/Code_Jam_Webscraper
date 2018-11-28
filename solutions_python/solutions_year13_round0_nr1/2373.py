def result(board):

	completed = True

	# check lines
	for i in range(4):

		if '.' in board[i]:
			completed = False

		if board[i].count('X') == 4 or (board[i].count('X') == 3 and board[i].count('T') == 1):
			return 'X won'

		if board[i].count('O') == 4 or (board[i].count('O') == 3 and board[i].count('T') == 1):
			return 'O won'


	#check columns
	for i in range(4):
		line = ""
		for j in range(4):
			line += board[j][i]

		if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
			return 'X won'

		if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
			return 'O won'


	#check diagonals
	diag1 = ""
	for i in range(4):
		diag1 += board[i][i]
	
	if diag1.count('X') == 4 or (diag1.count('X') == 3 and diag1.count('T') == 1):
			return 'X won'

	if diag1.count('O') == 4 or (diag1.count('O') == 3 and diag1.count('T') == 1):
			return 'O won'


	diag2 = ""
	j = 3
	for i in range(4):
		diag2 += board[j][i]
		j -= 1

	if diag2.count('X') == 4 or (diag2.count('X') == 3 and diag2.count('T') == 1):
			return 'X won'

	if diag2.count('O') == 4 or (diag2.count('O') == 3 and diag2.count('T') == 1):
			return 'O won'


	if completed:
		return 'Draw'
	return 'Game has not completed'


def main():
	f = open('/Users/alex/Downloads/A-large.in.txt')
	nTests = int(f.readline().replace("\n",""))

	for i in range(nTests):
		board = [["" for x in xrange(4)] for x in xrange(4)] 

		for j in range(4):
			line = f.readline()
			for k in range(4):
				board[j][k] = line[k]
		
		#print board

		f.readline() #empty line
		print "Case #" + str(i+1) + ": " + result(board)


if __name__ == "__main__":
    main()