cases = int(raw_input())
debug = False

winner = "RICHARD"

# check if Richard can choose an onimo that doesn't fit in the grid
def checkCheater(X, R, C):

	if X % 2 == 0:
		fixedX = X / 2
	else:
		fixedX = (X / 2) + 1

	if R < fixedX or C < fixedX:
		if debug:	print "Cheatable grid"
		return True
	else:
		return False


# check if Richard can create an onimo that can only be placed such that it blocks the grid
def checkBlocker(X, R, C):
	# block has to be larger than one of the sides
	if X <= R and X <= C:
		return False

	sumSides = (R + C)
	if sumSides % 2 == 0:
		sumSides -= 2
	else:
		sumSides -= 1

	# a blocking blok has to be able to reach both sides
	# which is (R + C) - 1 for uneven lengths and -2 for even lengths
	if X >= sumSides:
		return True
	else:
		return False



def printCase(case, winner):
	print "Case #" + str(case+1) + ": " + winner
	if debug:	print ""


for case in range(cases):
	X,R,C = raw_input().split()
	X = int(X)
	R = int(R)
	C = int(C)
	grid = R*C

	if debug:	print "[" + str(X) + "," + str(R) + "," + str(C) + "]"

	# with a grid too small for the first block, Richard wins
	if grid < X:
		if debug:	print "Can't even one block, so RICHARD wins"
		winner = "RICHARD"
		printCase(case, winner)
		continue

	# with N-omino's, gabriel always wins
	if X == 1:
		if debug:	print "Only one block, so Gabriel wins"
		winner = "GABRIEL"
		printCase(case, winner)
		continue

	# with two-omino's, the grid has to be of equal length for Gabriel to win
	if X == 2:
		if grid % 2 == 0:
			if debug:	print "Two and devidable, so Gabriel wins"
			winner = "GABRIEL"
			printCase(case, winner)
			continue
		else:
			if debug:	print "Two and can't devide, so Richard wins"
			winner = "RICHARD"
			printCase(case, winner)
			continue

	if (checkCheater(X,R,C)):
		if debug:	print "Can cheat this one, so Richard wins"
		winner = "RICHARD"
		printCase(case, winner)
		continue

	if (checkBlocker(X,R,C)):
		if debug:	print "Can create blocking-block, so Richard wins"
		winner = "RICHARD"
		printCase(case, winner)
		continue

	# the first block fits
	# if the remaining blocks are a multiple of X, Gabriel wins because she can just create blocks that fit in the remaining configuration
	remainingBlocks = grid - X
	if remainingBlocks % X == 0:
		if debug:	print "Devidable, so Gabriel wins"
		if debug: print "remainingBlocks: " + str(remainingBlocks)
		winner = "GABRIEL"
		printCase(case, winner)
		continue

	else:
		if debug:	print "Can't devide, so Richard wins"
		winner = "RICHARD"
		printCase(case, winner)
		continue
