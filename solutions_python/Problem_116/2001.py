import re

#	Get the file
f = open("A-large.in", "r")
q = open("A-large.out", "w")

f = f.readlines()

#	Get cases
cases = int(f[0])
case = 1

def gameIsFinished(game):
	#	loop through game to find any '.'
	for r in game:
		row = "".join(r)
		if row.find(".") != -1:
			return False

	return True



def checkRows(game):

	for row in game:
		if re.match('^[OOOT]+$', "".join(row)):
			return "O"

		elif re.match('^[XXXT]+$', "".join(row)):
			return "X"




def checkColumns(game):

	#	Contruct a string for each column
	c = 0
	while c < 4:

		column = ""

		for row in game:
			column += row[c]

		if re.match('^[OOOT]+$', column):
			return "O"

		elif re.match('^[XXXT]+$', column):
			return "X"

		c += 1



def checkDiag(game):

	diag = ""
	for s in range(4):
		diag += game[s][s]

	#	Check other diag
	h = 3
	diag2 = ""
	for g in range(4):
		diag2 += game[g][h-g]


	if re.match('^[OOOT]+$', diag) or re.match('^[OOOT]+$', diag2):
		return "O"

	if re.match('^[XXXT]+$', diag) or re.match('^[XXXT]+$', diag2):
		return "X"


#	Get the game board, store in multi dem array
#	Iterate through each row
for x in range(1, len(f), 5):

	game = list()

	j = 0
	while j < 4:
		row = list(f[x+j].strip('\n'))

		game.append(row)

		j += 1


	#	Game is received, determine the winner
	winner = checkRows(game)
	if winner == None:
		winner = checkColumns(game)
		if winner == None:
			winner = checkDiag(game)


	if winner == None:
		if gameIsFinished(game):
			q.write("Case #%s: Draw\n" % case)
		else:
			q.write("Case #%s: Game has not completed\n" % case)

	else:
		q.write("Case #%s: %s won\n" % (case, winner))


	case += 1









