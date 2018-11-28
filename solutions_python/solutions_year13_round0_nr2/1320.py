def validBoard(board):
	#print board
	for line in range(len(board)):
		for square in range(len(board[line])):
			if not squareValid(board, square, line):
				return False
	return True

def squareValid(board, x, y):
	row = board[y]
	col = [r[x] for r in board]
	#print board
	#print row
	#print col
	#print x, y
	return all([elem <= board[y][x] for elem in row]) or all([elem <= board[y][x] for elem in col])

size = "large"

f = open("B-{}.in".format(size), "r")
out = file("{}.out".format(size), "w")

lines = f.read().splitlines()[1:]

cases = []
output = []

currentLine = 0
while currentLine < len(lines):
	numLines = int(lines[currentLine].split(" ")[0])
	print numLines
	currentLine += 1

	case = []
	for line in lines[currentLine:currentLine + numLines]:
		case.append([int(i) for i in line.split(" ")])

	currentLine = currentLine + numLines
	cases.append(case)

currentCase = 1

for case in cases:
	if validBoard(case):
		output.append("YES")
	else:
		output.append("NO")

for outNum in range(len(output)):
	out.write("Case #{0}: {1}\n".format(outNum + 1, output[outNum]))
