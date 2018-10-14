import sys

data = open(sys.argv[1]).read().split("\n")

cases = int(data.pop(0))

board = []
for i in range(cases):
	board.append([data.pop(0) for i in range(4)])
	data.pop(0)
case = 1
for b in board:
	print "Case #%d:" % case,
	case += 1
	# Check diagonals.
	check = b[0][0]
	if check != ".":
		if check == "T": check = b[3][3]
		if all(map(lambda x: (x == check or x == "T") and x != ".", [b[i][i] for i in range(4)])):
			print "%s won" % check
			continue
	check = b[0][3]
	if check != ".":
		if check == "T": check = b[3][0]
		if all(map(lambda x: (x == check or x == "T") and x != ".", [b[i][3-i] for i in range(4)])):
			print "%s won" % check
			continue
	# Check rows
	for index in range(4):
		check = b[index][0]
		if check != ".":
			if check == "T": check = b[index][3]
		if all(map(lambda x: (x == check or x == "T") and x != ".", [b[index][i] for i in range(4)])):
			print "%s won" % check
			break
		check = b[0][index]
		if check != ".":
			if check == "T": check = b[3][index]
		if all(map(lambda x: (x == check or x == "T") and x != ".", [b[i][index] for i in range(4)])):
			print "%s won" % check
			break
	else:
		if all(map((lambda x: "." not in x), b)):
			print "Draw"
		else:
			print "Game has not completed"