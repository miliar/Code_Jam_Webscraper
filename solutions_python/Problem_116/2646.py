def tictac(fin, fout):
	fin = open(fin)
	fout = open(fout, "w")
	for i in range(int(fin.readline())):
		board = []
		for j in range(4):
			board.append(list(fin.readline()))
		fin.readline() #read blank line
		x = [True for j in range(10)]
		y = [True for j in range(10)]
		full = True
		for j in range(4):
			for k in range(4):
				if board[j][k] == "X" or board[j][k] == ".":
					y[j] = False
					y[4 + k] = False
					if j == k:
						y[8] = False
					elif j + k == 3:
						y[9] = False
				if board[j][k] == "O" or board[j][k] == ".":
					x[j] = False
					x[4 + k] = False
					if j == k:
						x[8] = False
					elif j + k == 3:
						x[9] = False
				if board[j][k] == ".":
					full = False
		if True in x:
			fout.write("Case #" + str(i + 1) +": X won\n")
		elif True in y:
			fout.write("Case #" + str(i + 1) +": O won\n")
		elif full:
			fout.write("Case #" + str(i + 1) +": Draw\n")
		else:
			fout.write("Case #" + str(i + 1) +": Game has not completed\n")

tictac("A-large.in", "output.txt")