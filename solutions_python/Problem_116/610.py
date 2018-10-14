def check(line):
	global incomplete, winner
	winner = ''

	for i in xrange(4):
		if line[i] == '.':
			incomplete = True
			break
		if line[i] == 'T':
			continue
		if winner == '':
			winner = line[i]
			continue
		if line[i] == winner:
			continue
		else:
			break
	else:
		return True

	return False

try:
	nTests = int(raw_input())

	for test in xrange(1, nTests+1):
		board = [raw_input() for _ in xrange(4)]
		zipboard = zip(*board)

		foundWinner = False
		incomplete = False

		if not foundWinner:
			for l in xrange(4):
				if check(board[l]):
					foundWinner = True
					break

		if not foundWinner:
			for c in xrange(4):
				if check(zipboard[c]):
					foundWinner = True
					break

		if not foundWinner:
			diag = [board[i][i] for i in xrange(4)]
			if check(diag):
				foundWinner = True

		if not foundWinner:
			diag = [board[-i-1][i] for i in xrange(4)]
			if check(diag):
				foundWinner = True

		if foundWinner:
			print "Case #%d: %s won" % (test, winner)
		elif incomplete:
			print "Case #%d: Game has not completed" % (test)
		else:
			print "Case #%d: Draw" % (test)

		raw_input()

except EOFError:
	pass
