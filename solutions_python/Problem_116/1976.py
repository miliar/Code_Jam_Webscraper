def fullBoard(table):
	for row in table:
		for item in row:
			if item == '.':
				return False
	return True

inFileName = 'Tic-Tac-Toe-Tomek-IN.txt'
outFileName = 'Tic-Tac-Toe-Tomek-OUT.txt'
f = open(inFileName)
cases = int (f.readline().rstrip())
tables = []
lines = f.readlines();
for case in range(cases):
	tables.append([])
	for line in range(4):
		tables[case].append([])
		for c in range(4):
			tables[case][line].append(lines[(case)*5 + line].rstrip()[c])
f.close()
f = open(outFileName, 'w')
case = 1
for table in tables:
	xwin = False
	owin = False
	# Check rows
	for row in range(4):
		for column in range(4):
			if not (table[row][column] == 'X' or table[row][column] == 'T'):
				break
			if column == 3: 
				xwin = True
		for column in range(4):
			if not (table[row][column] == 'O' or table[row][column] == 'T'):
				break
			if column == 3:
				owin = True

	# Check columns 
	for column in range(4):
		for row in range(4):
			if not (table[row][column] == 'X' or table[row][column] == 'T'):
				break
			if row == 3: 
				xwin = True
		for row in range(4):
			if not (table[row][column] == 'O' or table[row][column] == 'T'):
				break
			if row == 3: 
				owin = True

	# Check diagonals
	row = 0
	column = 0
	for _ in range(4):
		if not (table[row][column] == 'X' or table[row][column] == 'T'):
			break
		if row == 3: 
			xwin = True
		row += 1
		column += 1
	row = 0
	column = 0
	for _ in range(4):
		if not (table[row][column] == 'O' or table[row][column] == 'T'):
			break
		if row == 3: 
			owin = True
		row += 1
		column += 1
	row = 0
	column = 3
	for _ in range(4):
		if not (table[row][column] == 'X' or table[row][column] == 'T'):
			break
		if row == 3: 
			xwin = True
		row += 1
		column -= 1
	row = 0
	column = 3
	for _ in range(4):
		if not (table[row][column] == 'O' or table[row][column] == 'T'):
			break
		if row == 3: 
			owin = True
		row += 1
		column -= 1

	if (xwin and owin) or (fullBoard(table) and not (xwin or owin)):
		f.write("Case #" + str(case) + ": Draw\n")
	elif xwin:
		f.write("Case #" + str(case) + ": X won\n")
	elif owin:
		f.write("Case #" + str(case) + ": O won\n")
	else:
		f.write("Case #" + str(case) + ": Game has not completed\n")
	case += 1
f.close()