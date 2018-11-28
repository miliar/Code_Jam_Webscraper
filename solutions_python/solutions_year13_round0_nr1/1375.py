zf = [0,1,2,3]

testCases = input()
for testCase in xrange(0, testCases):
	if testCase != 0: raw_input()
	# read Board
	board = []
	for i in zf:
		board.append(raw_input())
	for winChar in ['X', 'O']:
		win = False
		#  check rows
		for i in zf:
			win = True
			for j in zf:
				if board[i][j] != winChar and board[i][j] != 'T':
					win = False
					break
			if win: break
		# print win
		if win: break
		# print "A"
		# check cols
		for i in zf:
			win = True
			for j in zf:
				# print board[j][i]
				if board[j][i] != winChar and board[j][i] != 'T':
					win = False
					break
			# print win
			if win: break
		# print win
		if win: break

		# check diags
		win = True
		for i in zf:
			if board[i][i] != winChar and board[i][i] != 'T':
				win = False
				break
		# print win
		if win: break

		win = True
		for i in zf:
			# print board[i][3 - i]
			if board[i][3 - i] != winChar and board[i][3 - i] != 'T':
				win = False
				break
		# print win
		if win: break
	if win:
		print "Case #%d: %s won" % (testCase + 1, winChar)
		continue

	if ''.join(board).find('.') == -1:
		print "Case #%d: Draw" % (testCase + 1)
	else:
		print "Case #%d: Game has not completed" % (testCase + 1)
		



# Case #1: X won
# Case #2: Draw
# Case #3: Game has not completed
# Case #4: O won
# Case #5: O won
# Case #6: O won
