
def rotate(board, n):
	for i in range(0, n):
		first_free = n-1
		while first_free >= 0:
			if board[i][first_free] == '.':
				break
			first_free -= 1
		for j in range(first_free, -1, -1):
			if board[i][j] != '.':
				board[i][first_free] = board[i][j]
				board[i][j] = '.'

				first_free -= 1

	return board

def check_for_win(board, n, t, c):
	red_won = False
	blue_won = False
	for i in range(0, n):
		for j in range(0, n):
			cur_val = board[i][j]
			if cur_val == '.':
				continue
			if cur_val == 'R' and red_won:
				continue
			if cur_val == 'B' and blue_won:
				continue

			cur_won = [j+t-1 < n, i+t-1 < n, j+t-1 < n and i+t-1 < n, i-t+1 >= 0 and j+t-1 < n]
			for k in range(1, t):
				if cur_won[0] and board[i][j+k] != cur_val:
					cur_won[0] = False
				if cur_won[1] and board[i+k][j] != cur_val:
					cur_won[1] = False
				if cur_won[2] and board[i+k][j+k] != cur_val:
					cur_won[2] = False
				if cur_won[3] and board[i-k][j+k] != cur_val:
					cur_won[3] = False
			if reduce(lambda a, b: a or b, cur_won):
				if cur_val == 'R':
					red_won = True
				else:
					blue_won = True

	if red_won and blue_won:
		return 'Both'
	elif red_won:
		return 'Red'
	elif blue_won:
		return 'Blue'
	else:
		return 'Neither'

for c in range(1, input()+1):
	n, k = [int(d) for d in raw_input().split(' ')]
	board = []
	for l in range(0, n):
		board.append(list(raw_input()))

	board = rotate(board, n)
	res = check_for_win(board, n, k, c)
	print "Case #%d: %s" % (c, res)
