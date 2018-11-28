# Read input text file - Check
# Determine game state
# Output result of game state

file = open("A-large.in.txt", 'r')
T = file.readline()
T = int(T)
count = 0
case_number = 1



# iterate for each test case
while (count < T):
	board = [0, 1, 2, 3]
	diag1 = [0, 1, 2, 3]
	diag2 = [0, 1, 2, 3]
	spot = ''
	extra = ''
	status = ''
	draw_check = ''
	
	# Read in each test case as a list of lists
	for line in range(0, 4):
		board[line] = list(file.readline().rstrip())
	
	# All . check
	spot = '.'
	dot_check = 0
	for line in board:
		for square in line:
			if (square == '.'):
				dot_check += 1
	if (dot_check == 16):
		print "Case #" + str(case_number) + ": " + "Game has not completed"
		status = 'won'
	
	# horizontal check
	if (status != 'won'):
		for line in board:
			if (line[0] == 'T'):
				spot = line[1]
			else:
				spot = line[0]
			horz_check = 0
			for square in line:
				if (square == spot or square == 'T'):
					horz_check += 1
			if (horz_check == 4 and spot != '.'):
				print "Case #" + str(case_number) + ": " + str(spot) + " won"
				status = 'won'
	
	# vertical check
	if (status != 'won'):
		for x in range(0, 4):
			spot = ''
			vert_check = 0
			for line in board:
				if (spot == ''):
					if (line[x] == 'T'):
						spot = ''
					else:
						spot = line[x]
					vert_check += 1
				elif (line[x] == spot or line[x] == 'T'):
					vert_check += 1
			if (vert_check == 4 and spot != '.'):
				print "Case #" + str(case_number) + ": " + str(spot) + " won"
				status = 'won'
	
	# diagonal check
	if (status != 'won'):
		diag_place = 3
		list_place = 0
		for line in board:
			diag1[list_place] = line[diag_place]
			list_place += 1
			diag_place -= 1
	
		diag_place = 0
		list_place = 3
		for line in board:
			diag2[list_place] = line[diag_place]
			list_place -= 1
			diag_place += 1
	
		diag_check = 0
		if (diag1[0] == 'T'):
			spot = diag1[1]
		else:
			spot = diag1[0]
		for x in diag1:
			if (x == spot or x == 'T'):
				diag_check += 1
		if (diag_check == 4 and spot != '.'):
			print "Case #" + str(case_number) + ": " + str(spot) + " won"
			status = 'won'

		diag_check = 0
		if (diag2[0] == 'T'):
			spot = diag2[1]
		else:
			spot = diag2[0]
		for x in diag2:
			if (x == spot or x == 'T'):
				diag_check += 1
		if (diag_check == 4 and spot != '.'):
			print "Case #" + str(case_number) + ": " + str(spot) + " won"
			status = 'won'
	
	# check for draw if no decision
	if (status != 'won'):
		for line in board:
			for square in line:
				if (square == '.'):
					draw_check = 'no'
		if (draw_check == 'no'):
			print "Case #" + str(case_number) + ": " + "Game has not completed"
		else:
			print "Case #" + str(case_number) + ": " + "Draw" 
	
	extra = file.readline()
	count += 1
	case_number += 1

	