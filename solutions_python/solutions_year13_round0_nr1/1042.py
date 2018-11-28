import sys

def check_winner(B):
	# Check for win.
	for player in ['O', 'X']:
		# Rows
		for i in xrange(4):
			win = True
			for j in xrange(4):
				if (B[i][j] != player) and (B[i][j] != 'T'):
					win = False
			if win:
				return player + " won"

		# Cols
		for j in xrange(4):
			win = True
			for i in xrange(4):
				if (B[i][j] != player) and (B[i][j] != 'T'):
					win = False
			if win:
				return player + " won"

		# Main diag
		win = True
		for i in xrange(4):
			if (B[i][i] != player) and (B[i][i] != 'T'):
				win = False
		if win:
			return player + " won"

		# Sec diag
		win = True
		for i in xrange(4):
			if (B[i][3 - i] != player) and (B[i][3 - i] != 'T'):
				win = False
		if win:
			return player + " won"


	# Check for draw.
	for i in xrange(4):
		for j in xrange(4):
			if B[i][j] == '.':
				return "Game has not completed"
	return "Draw"

in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[1] + ".out", "w")

T = int(in_file.readline())

for i in xrange(T):
	B = []

	for j in xrange(4):
		B.append(in_file.readline())
	in_file.readline()

	winner = check_winner(B)

	out_file.write("Case #" + str(i + 1) + ": " + winner + "\n")

in_file.close()
out_file.close()



