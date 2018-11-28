t = int(raw_input())
for case in xrange(t):
	board = []
	for _ in xrange(4):
		board.append(raw_input())
	raw_input()
	finished = True
	winner = None
	diag1 = [board[x][x] for x in xrange(4)]
	diag2 = [board[x][-x-1] for x in xrange(4)]
	if (diag1.count('X') + diag1.count('T') == 4) or (diag2.count('X') + diag2.count('T') == 4):
		winner = 'X'
	elif (diag1.count('O') + diag1.count('T') == 4) or (diag2.count('O') + diag2.count('T') == 4):
		winner = 'O'
	else:
		for j, row in enumerate(board):
			if row.count('X') + row.count('T') == 4:
				winner = 'X'
				break
			elif row.count('O') + row.count('T') == 4:
				winner = 'O'
				break
		else:
			for i in xrange(4):
				col = [board[x][i] for x in xrange(4)]
				if col.count('X') + col.count('T') == 4:
					winner = 'X'
					break
				elif col.count('O') + col.count('T') == 4:
					winner = 'O'
					break
				elif col.count('.') > 0:
					finished = False
	if winner:
		print "Case #" + str(case + 1) + ": " + winner + " won"
	elif finished:
		print "Case #" + str(case + 1) + ": Draw"
	else:
		print "Case #" + str(case + 1) + ": Game has not completed"