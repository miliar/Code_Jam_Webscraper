import sys

numCases = int(raw_input()) # get the number of cases 
x = 1

while(x <= numCases):
	board = []

	# this loop will read in our 4x4 board
	for i in xrange(4):
		line = sys.stdin.readline()
		line = list(line.split())
		board.append(line)

	otherLine = sys.stdin.readline().split() # this is so we don't get any bullshit newline indices
	# print board

	# now it's time to figure out what the status of the board is

	# first we'll check to see if it's empty and whether there are enough moves to declare a winner
	emptyCount = 0
	oCount = 0
	xCount = 0

	for i in xrange(4):
		for j in xrange(4):
			if(board[i][0][j] == '.'):
				emptyCount = emptyCount + 1
			elif(board[i][0][j] == 'O'):
				oCount = oCount + 1
			elif(board[i][0][j] == 'X'):
				xCount = xCount + 1

	# print "X: " + str(xCount) + "  O: " + str(oCount) + "  Empty: " + str(emptyCount)

	# now here come the loops!!!!!!!!!!!!!
	won = False

	# check to see if anyone won the horizontals
	for i in xrange(4):
		horiz = list(board[i][0])
		# print horiz

		if 'T' in horiz:
			horiz.remove('T')
			if(horiz[0] == horiz[1] == horiz[2]):
				if(horiz[0] == 'O'):
					print "Case #" + str(x) + ": O won"
					won = True
					break;
				elif(horiz[0] == 'X'):
					print "Case #" + str(x) + ": X won"
					won = True
					break;
		else:
			if(horiz[0] == horiz[1] == horiz[2] == horiz[3]):
				if(horiz[0] == 'O'):
					print "Case #" + str(x) + ": O won"
					won = True
					break;
				elif(horiz[0] == 'X'):
					print "Case #" + str(x) + ": X won"
					won = True
					break;

	if(won == True):
		x = x + 1
		continue

	# print('\n')

	# now check verticals
	for i in xrange(4):
		verts = []
		for j in xrange(4):
			verts.append(board[j][0][i])
		# print verts
		if 'T' in verts:
			verts.remove('T')
			if(verts[0] == verts[1] == verts[2]):
				if(verts[0] == 'O'):
					print "Case #" + str(x) + ": O won"
					won = True
					break
				elif(verts[0] == 'X'):
					print "Case #" + str(x) + ": X won"
					won = True
					break
		else:
			if(verts[0] == verts[1] == verts[2] == verts[3]):
				if(verts[0] == 'O'):
					print "Case #" + str(x) + ": O won"
					won = True
					break
				elif(verts[0] == 'X'):
					print "Case #" + str(x) + ": X won"
					won = True
					break

	if(won == True):
		x = x + 1
		continue

	# print('\n')

	# and now for the diagonals!
	diag1 = []
	for i in xrange(4):
		diag1.append(board[i][0][i])
	# print diag1
	if 'T' in diag1:
		diag1.remove('T')
		if(diag1[0] == diag1[1] == diag1[2]):
			if(diag1[0] == 'O'):
				print "Case #" + str(x) + ": O won"
				won = True
			elif(diag1[0] == 'X'):
				print "Case #" + str(x) + ": X won"
				won = True
	else:
		if(diag1[0] == diag1[1] == diag1[2] == diag1[3]):
			if(diag1[0] == 'O'):
				print "Case #" + str(x) + ": O won"
				won = True
			elif(diag1[0] == 'X'):
				print "Case #" + str(x) + ": X won"
				won = True

	if(won == True):
		x = x + 1
		continue

	# print('\n')

	diag2 = []
	for i in xrange(4):
		diag2.append(board[i][0][3 - i])
	# print diag2
	if 'T' in diag2:
		diag2.remove('T')
		if(diag2[0] == diag2[1] == diag2[2]):
			if(diag2[0] == 'O'):
				print "Case #" + str(x) + ": O won"
				won = True
			elif(diag2[0] == 'X'):
				print "Case #" + str(x) + ": X won"
				won = True
	else:
		if(diag2[0] == diag2[1] == diag2[2] == diag2[3]):
			if(diag2[0] == 'O'):
				print "Case #" + str(x) + ": O won"
				won = True
			elif(diag2[0] == 'X'):
				print "Case #" + str(x) + ": X won"
				won = True

	if not won:
		if(emptyCount == 0):
			print "Case #" + str(x) + ": Draw"
		else:
			print "Case #" + str(x) + ": Game has not completed"

	x = x + 1