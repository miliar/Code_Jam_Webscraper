import sys

def winnerForList(inList):
	listSum = sum(inList)
	if listSum == 13 or listSum == 4:
		return 1
	elif listSum == 7 or listSum == -4:
		return -1
	return 0


if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for _t in xrange(t):
		winner = 0
		emptyfound = False
		rows = list()
		for _row in xrange(4):
			line = f.readline()

			if winner != 0:
				continue

			column = list()
			for _i in xrange(4):
				if (line[_i] == 'X'):
					column.append(1)
				elif (line[_i] == 'O'):
					column.append(-1)
				elif (line[_i] == 'T'):
					column.append(10)
				else:
					emptyfound = True
					column.append(0)
			rows.append(column)

			winner = winnerForList(column)

		if winner == 0:
			for _row in zip(*rows):
				winner = winnerForList(_row)
				if winner != 0:
					break

		if winner == 0:
			winner = winnerForList([rows[0][0], rows[1][1], rows[2][2], rows[3][3]])
		if winner == 0:
			winner = winnerForList([rows[0][3], rows[1][2], rows[2][1], rows[3][0]])

		if winner == 1:
			print "Case #%d: X won" % (_t + 1)
		elif winner == -1:
			print "Case #%d: O won" % (_t + 1)
		elif emptyfound:
			print "Case #%d: Game has not completed" % (_t + 1)
		else:
			print "Case #%d: Draw" % (_t + 1)

		# prepare to read next set
		f.readline()