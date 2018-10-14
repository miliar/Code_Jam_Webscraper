kb = []
output = open('C:/googlers.in', 'w')

def read(path):
	output = open('googlers.in', 'w')
	x = 1
	fill = "fill"
	f = open(path)
	numtrials = f.readline()
	numtrials = 1000
	while x <= numtrials:
		won = False
		answer = "Case #" + str(x) + ": Game has not completed"
		line = f.readline()
		linesep1 = [line[:1], line[1:2], line[2:3], line[3:4]]
		
		line = f.readline()
		linesep2 = [line[:1], line[1:2], line[2:3], line[3:4]]
		
		line = f.readline()
		linesep3 = [line[:1], line[1:2], line[2:3], line[3:4]]
		
		line = f.readline()
		linesep4 = [line[:1], line[1:2], line[2:3], line[3:4]]
		f.readline()
		
		board = [linesep1, linesep2, linesep3, linesep4]
		
		if not ("." in linesep1 or "." in linesep2 or "." in linesep3 or "." in linesep4):
			answer = "Case #" + str(x) + ": Draw"
		for row in board:
			if "." in row:
				string = "fill"
			elif row[0] == row[1] and row[1] == row[2] and row[2] == row[3] and row[0] != ".":
				answer =  "Case #" + str(x) + ": " + row[0] + " won"
				won = True
			elif "X" in row and "O" in row:
				string = "fill"
			else:
				if row[0] != "T":
					answer =  "Case #" + str(x) + ": " + row[0] + " won"
					won = True
				else:
					answer =  "Case #" + str(x) + ": " + row[1] + " won"
					won = True
		run = 0
		while run < 4:
			first = board[0][run]
			second = board[1][run]
			third = board[2][run]
			fourth = board[3][run]
			run += 1
			if first == "." or second == "." or third == "." or fourth == ".":
				string = "filler"
			elif first == "T" and second == third == fourth:
				answer = "Case #" + str(x) + ": " + second + " won"
				won = True
			elif second == "T" and first == third == fourth:
				answer = "Case #" + str(x) + ": " + first + " won"
				won = True
			elif third == "T" and first == second == fourth:
				answer = "Case #" + str(x) + ": " + first + " won"
				won = True
			elif fourth == "T" and first == second == third:
				answer = "Case #" + str(x) + ": " + first + " won"
				won = True
			elif first == second == third == fourth:
				answer = "Case #" + str(x) + ": " + first + " won"
		diag = board[0][0] + board[1][1] + board[2][2] + board[3][3]
		diag2 = board[3][0] + board[2][1] + board[1][2] + board[0][3]
		if "." in diag:
			string = fill
		if "." in diag2:
			string = fill
		if not ("X" in diag and "O" in diag) and not "." in diag:
			if board[0][0] == "T":
				answer = "Case #" + str(x) + ": " + board[1][1] + " won"
				won = True
			else:
				answer = "Case #" + str(x) + ": " + board[0][0] + " won"
				won = True
		elif not ("X" in diag2 and "O" in diag2) and not "." in diag2:
			if board[3][0] == "T":
				answer = "Case #" + str(x) + ": " + board[2][1] + " won"
			else:
				answer = "Case #" + str(x) + ": " + board[3][0] + " won"
		output.write(answer)
		output.write("\n")
		x += 1
	output.close()