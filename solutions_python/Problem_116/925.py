def winner(game):
	#diagonal
	xc = 0
	oc = 0
	tc = 0
	for i in range(4):
		xc += game[i][i] == "X"
		oc += game[i][i] == "O"
		tc += game[i][i] == "T"
	if xc+tc == 4:
		return "X won"
	elif oc+tc == 4:
		return "O won"

	#other diagonal
	xc = 0
	oc = 0
	tc = 0
	for i in range(4):
		xc += game[i][3-i] == "X"
		oc += game[i][3-i] == "O"
		tc += game[i][3-i] == "T"
	if xc+tc == 4:
		return "X won"
	elif oc+tc == 4:
		return "O won"

	#lines
	for line in game:
		xc = 0
		oc = 0
		tc = 0
		for move in line:
			xc += "X" == move
			oc += "O" == move
			tc += "T" == move
		if xc+tc == 4:
			return "X won"
		elif oc+tc == 4:
			return "O won"

	#columns
	mc = 0
	for i in range(4):
		xc = 0
		oc = 0
		tc = 0
		for j in range(4):
			move = game[j][i]
			xc += "X" == move
			oc += "O" == move
			tc += "T" == move
			mc += "." != move
		if xc+tc == 4:
			return "X won"
		elif oc+tc == 4:
			return "O won"
	if mc == 16:
		return "Draw"
	else:
		return "Game has not completed"

lines = [line.strip() for line in open('A-large.in.txt')]
n = int(lines[0])
start = 1
end = 5
for i in range(n):
	print "Case #" + str(i+1) + ": " + winner(lines[start:end])
	start = start + 5
	end = start + 4