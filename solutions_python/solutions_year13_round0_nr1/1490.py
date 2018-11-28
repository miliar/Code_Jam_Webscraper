def winnerOfLine(elems):
	winner = None
	for elem in elems:
		if elem == ".":
			return None

		if winner == None:
			if elem in ["X", "O"]:
				winner = elem
		elif elem != winner and elem != "T":
			return None

	return winner + " won"

def winnerOfBoard(board):
	for hLine in board:
		if winnerOfLine(hLine):
			return winnerOfLine(hLine)

	for vLine in range(len(board[0])):
		test = [line[vLine] for line in board]

		if winnerOfLine(test):
			return winnerOfLine(test)

	diag1 = []
	diag2 = []
	for diag in range(len(board)):
		diag1.append(board[diag][diag])
		diag2.append(board[diag][-(diag + 1)])

	#print diag1
	#print diag2

	if winnerOfLine(diag1):
		return winnerOfLine(diag1)
	if winnerOfLine(diag2):
		return winnerOfLine(diag2)

	for line in board:
		if "." in line:
			return "Game has not completed"
	return "Draw"


size = "large"

f = open("A-{}.in".format(size), "r")
out = file("{}.out".format(size), "w")

lines = f.read().splitlines()[1:]

cases = []
output = []

for i in range(0, len(lines), 5):
	board = lines[i:i + 4]

	cases.append(board)

currentCase = 1

for case in cases:
	output.append(winnerOfBoard(case))

for outNum in range(len(output)):
	out.write("Case #{0}: {1}\n".format(outNum + 1, output[outNum]))