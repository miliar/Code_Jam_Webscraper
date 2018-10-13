def is_winner(player, board):
	for row in board:
		if not row.replace(player, "").replace("T", ""): return True
	for index in xrange(4):
		col = "".join([row[index] for row in board])
		if not col.replace(player, "").replace("T", ""): return True
	diagonal = "".join([board[index][index] for index in xrange(4)])
	if not diagonal.replace(player, "").replace("T", ""): return True
	diagonal = "".join([board[index][3 - index] for index in xrange(4)])
	if not diagonal.replace(player, "").replace("T", ""): return True
	return False

for case in xrange(1, int(raw_input()) + 1):
	if case > 1: raw_input()
	board, full = [], True
	for x in xrange(4):
		row = raw_input()
		board.append(row)
		if full and "." in row: full = False
	status = "Draw" if full else "Game has not completed"
	if is_winner("X", board): status = "X won"
	elif is_winner("O", board): status = "O won"
	print "Case #%d: %s" % (case, status)