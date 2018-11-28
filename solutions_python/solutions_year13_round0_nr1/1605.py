


INPUT_SAMPLE = 'tic_tac_sample_input.txt'
INPUT_SMALL  = 'tic_tac_input_small.txt'

INPUT = INPUT_SMALL
CHECK_WITH_T_IN_MIDDLE = False


GAME_X_WON = "X won"
GAME_O_WON = "O won"
GAME_DRAW  = "Draw"
GAME_NOT_COMPLETED = "Game has not completed"



# After a player's move, if there is a row, column or a diagonal
# containing 4 of that player's symbols,
# or containing 3 of her symbols and the 'T' symbol,
# she wins and the game ends.
# Otherwise the game continues with the other player's move.
# If all of the fields are filled with symbols and nobody won,
# the game ends in a draw.


# returns "X" if X has a winning combination
# returns "O" if O has a winning combination
# returns None if nobody has a winning combination
def checkStatusOfRow(row, checkWithTInMiddle):
	if ("XXXX" in row) or\
		("XXXT" in row) or\
		("TXXX" in row):
		return GAME_X_WON
	if ("OOOO" in row) or\
		("OOOT" in row) or\
		("TOOO" in row):
		return GAME_O_WON

	if checkWithTInMiddle:
		if ("XXTX" in row) or\
			("XTXX" in row):
			return GAME_X_WON
		if ("OOTO" in row) or\
			("OTOO" in row):
			return GAME_O_WON

	return None


f = open("output.txt", 'w')

lines = open(INPUT, 'r').readlines()

lines = [x.rstrip('\n') for x in lines]

noTestCases = int(lines[0])
lines = lines[1:]


for currTestCase in xrange(0, noTestCases):
	if (currTestCase !=0):
		f.write("\n")

	f.write('Case #' + str(currTestCase+1) + ": ")
	# 4 lines followed by a blank line
	idx = currTestCase * 5

	board = [lines[idx],lines[idx+1],lines[idx+2],lines[idx+3]]
	b = board

	completed = None
	tuplesToCheck = []

	# add the horizontal lines
	tuplesToCheck = b

	# add the vertical columns
	for col_no in xrange(0,4):
		col = b[0][col_no] + b[1][col_no] + b[2][col_no] + b[3][col_no]
		tuplesToCheck.append(col)

	# add the diagonals, top left -> bottom right
	diag = b[0][0] + b[1][1] + b[2][2] + b[3][3]
	tuplesToCheck.append(diag)

	diag = b[0][3] + b[1][2] + b[2][1] + b[3][0]
	tuplesToCheck.append(diag)

	for tuple_to_check in tuplesToCheck:

		status = checkStatusOfRow(tuple_to_check, CHECK_WITH_T_IN_MIDDLE)

		if status is not None:
			completed = status
			break

	# see if we've finished
	if completed is not None:
		f.write(completed)
		continue

	# that means we haven't found a winner

	# if there is an empty space '.', then the game is not finished

	if '.' in b[0] or '.' in b[1] or '.' in b[2] or '.' in b[3] :
		f.write(GAME_NOT_COMPLETED)
	else:
		f.write(GAME_DRAW)


