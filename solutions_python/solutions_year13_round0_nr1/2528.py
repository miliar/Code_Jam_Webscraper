cases = input()
for case in range(cases):
	board = [ raw_input() for line in range(5) ]
	# Horizontal
	# X won
	if any([ True for row in board if row.replace('T', 'X') == 'XXXX' ]):
		print 'Case #%d: X won' % (case + 1)
		continue

	# O won
	if any([ True for row in board if row.replace('T', 'O') == 'OOOO' ]):
		print 'Case #%d: O won' % (case + 1)
		continue

	# Vertical
	# X won
	if any([ (len([ True for j in range(4) if board[j][i] in 'XT' ]) == 4) for i in range(4) ]):
		print 'Case #%d: X won' % (case + 1)
		continue

	# O won
	if any([ (len([ True for j in range(4) if board[j][i] in 'OT' ]) == 4) for i in range(4) ]):
		print 'Case #%d: O won' % (case + 1)
		continue

	# Diagonal
	# X won
	if (''.join([ board[i][i] for i in range(4) ])).replace('T', 'X') == 'XXXX':
		print 'Case #%d: X won' % (case + 1)
		continue

	if (board[0][3] + board[1][2] + board[2][1] + board[3][0]).replace('T', 'X') == 'XXXX':
		print 'Case #%d: X won' % (case + 1)
		continue

	# O won
	if (''.join([ board[i][i] for i in range(4) ])).replace('T', 'O') == 'OOOO':
		print 'Case #%d: O won' % (case + 1)
		continue

	if (board[0][3] + board[1][2] + board[2][1] + board[3][0]).replace('T', 'O') == 'OOOO':
		print 'Case #%d: O won' % (case + 1)
		continue

	# Draw
	if (''.join(board)).find('.') == -1:
		print 'Case #%d: Draw' % (case + 1)
		continue

	# Game has not completed
	if (''.join(board)).find('.') != -1:
		print 'Case #%d: Game has not completed' % (case + 1)
		continue
