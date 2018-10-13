cases = int(raw_input())
for case in xrange(1, cases+1):
	result = "Draw"
	blank = 0
	board = ["", "", "", ""]
	# board[row][column]
	for row in xrange(0, 4):
		board[row] = raw_input()
		if board[row] == "":
			board[row] = raw_input()
	for row in xrange(0, 4):
		yay = 0
		for col in xrange(0, 4):
			if board[row][col] == "X" or board[row][col] == "T":
				yay += 1
		if yay == 4:
			result = "X won"
	for col in xrange(0, 4):
		yay = 0
		for row in xrange(0, 4):
			if board[row][col] == "X" or board[row][col] == "T":
				yay += 1
		if yay == 4:
			result = "X won"
	yay = 0
	for diag in xrange(0, 4):
		if board[diag][diag] == "X" or board[diag][diag] == "T":
			yay += 1
	if yay == 4:
		result = "X won"
	yay = 0
	for diag in xrange(0, 4):
		if board[diag][3-diag] == "X" or board[diag][3-diag] == "T":
			yay += 1
	if yay == 4:
		result = "X won"
	if result == "X won":
		print "Case #"+str(case)+":", result
		continue

	for row in xrange(0, 4):
		yay = 0
		for col in xrange(0, 4):
			if board[row][col] == "O" or board[row][col] == "T":
				yay += 1
		if yay == 4:
			result = "O won"
	for col in xrange(0, 4):
		yay = 0
		for row in xrange(0, 4):
			if board[row][col] == "O" or board[row][col] == "T":
				yay += 1
		if yay == 4:
			result = "O won"
	yay = 0
	for diag in xrange(0, 4):
		if board[diag][diag] == "O" or board[diag][diag] == "T":
			yay += 1
	if yay == 4:
		result = "O won"
	yay = 0
	for diag in xrange(0, 4):
		if board[diag][3-diag] == "O" or board[diag][3-diag] == "T":
			yay += 1
	if yay == 4:
		result = "O won"
	if result == "O won":
		print "Case #"+str(case)+":", result
		continue
	
	for row in xrange(0, 4):
		for col in xrange(0, 4):
			if board[row][col] == ".":
				blank = 1
	if blank:
		result = "Game has not completed"
	else:
		result = "Draw"
	print "Case #"+str(case)+":", result


