def check(path="input.txt"):
	input_file = open(path)
	result = open("output.txt", "w")
	cases = int(input_file.readline())
	for i in range(cases):
		board = []
		for n in range(4):
			l = input_file.readline()
			board.append(l[:-1])
		output = "Case #%s: %s\n" % (i+1, check_tic_tac_toe(board))
		print output
		result.write(output)
		input_file.readline()

	input_file.close()
	result.close()


def check_tic_tac_toe(tic):
	#TODO - add work with diagonals
	inverted = [""]*4
	diagonals = [""]*2
	dots = False#flag set to True if board is not finished
	for r in tic:
		checked = check_tic_tac_line(r)
		if checked[0]:
			return checked[1]
		else:
			if checked[1] == ".":
				dots = True
			for i in range(4):
				inverted[i] += r[i]#Create list with vertical lines
	counter = 0
	for r in inverted:
		checked = check_tic_tac_line(r)
		if checked[0]:
			return checked[1]
		#Create list with diagonals
		diagonals[0] += r[0 + counter]
		diagonals[1] += r[3 - counter]
		counter += 1

	for r in diagonals:
		checked = check_tic_tac_line(r)
		if checked[0]:
			return checked[1]

	if dots:
		return "Game has not completed"
	else:
		return "Draw"

def check_tic_tac_line(s):
	"""(str) -> (bool, "message")
	>>>check_tic_tac_line("XXXX")
	(True, "X won")
	>>>check_tic_tac_line("XX.X")
	(False, ".")
	>>>check_tic_tac_line("OOTO")
	(True, "O won")
	"""
	x = "XXXX"
	o = "OOOO"
	x_won = (True, "X won")
	o_won = (True, "O won")
	if s == x:
		return x_won
	elif s == o:
		return o_won
	elif "T" in s:
		if s.count("X") == 3:
			return x_won
		elif s.count("O") == 3:
			return o_won
	elif "." in s:
		return (False, ".")

	return (False, "")

# tic = ["XXXX", "OOOO", "XTXX", "O.OO", "TOOO"]
# for t in tic:
# 	print check_tic_tac_line(t)

# board = ["XXXT", "....", "OO..", "...."]
# board_1 = ["X...", ".X..", "..X.", "...X"]
# board_2 = ["X...", ".O..", "..X.", "...X"]
# print check_tic_tac_toe(board)
# print check_tic_tac_toe(board_1)
# print check_tic_tac_toe(board_2)
check("A-small-attempt0.in")
