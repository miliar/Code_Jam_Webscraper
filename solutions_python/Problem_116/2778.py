def allSame(astring):
	isx = True
	for i in astring:
		if i != "X" and i != "T":
			if i == ".":
				return 2
			isx = False
			break
	if isx:
		return 0
	iso = True
	for i in astring:
		if i != "O" and i != "T":
			if i == ".":
				return 2
			iso = False
			break
	if iso:
		return 1
	return 3
myin = open("tictactoe.in", "r")
num = int(myin.readline()[:-1])
data = []
for i in range(num):
	data.append([])
	for a in range(4):
		data[-1].append(myin.readline()[:-1])
	myin.readline()
myout = open("tictactoe.out", "w")
for i in range(len(data)):
	state = 3
	shouldstop = False
	for a in range(4):
		astring = ""
		for b in range(4):
			astring += data[i][a][b]
		state1 = allSame(astring)
		if state1 < state:
			state = state1
		if state == 0 or state == 1:
			shouldstop = True
			break
	if not shouldstop:
		shouldstop = False
		for a in range(4):
			astring = ""
			for b in range(4):
				astring += data[i][b][a]
			state1 = allSame(astring)
			if state1 < state:
				state = state1
			if state == 0 or state == 1:
				shouldstop = True
				break
		if not shouldstop:
			state1 = allSame(data[i][0][0] + data[i][1][1] + data[i][2][2] + data[i][3][3])
			if state1 < state:
				state = state1
			state1 = allSame(data[i][3][0] + data[i][2][1] + data[i][1][2] + data[i][0][3])
			if state1 < state:
				state = state1
	if state == 0:
		myout.write("Case #" + str(i + 1) + ": X won\n")
	elif state == 1:
		myout.write("Case #" + str(i + 1) + ": O won\n")
	elif state == 2:
		myout.write("Case #" + str(i + 1) + ": Game has not completed\n")
	else:
		myout.write("Case #" + str(i + 1) + ": Draw\n")
