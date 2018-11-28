from sys import stdin

def parse2Darray(numRow):
	arr = [[] for i in range(numRow)]
	for i in range(numRow):
		arr[i] = list(stdin.readline().strip())
	return arr

def checkRow(row):
	numCons = 0
	last = ''
	hasBlank = 0
	for i in range(4):
		if row[i] == '.':
			hasBlank = 1
			numCons = 0
			last = ''
		elif row[i] != last and row[i] != 'T':
			last = row[i]
			numCons = 1
		else:
			numCons += 1
		if numCons == 4:
			return last
	if hasBlank:
		return '.'
	return ''

T = int(stdin.readline())
for t in range(T):
	table = parse2Darray(4)
	stdin.readline()
	result = ''
	hasBlank = 0

	# check row
	for i in range(4):
		row = table[i]
		result = checkRow(row)
		if result == 'X' or result == 'O':
			break;
		elif result == '.':
			hasBlank = 1

	if result != 'X' and result != 'O':			
		# check col
		for j in range(4):
			row = []
			for i in range(4):
				row.append(table[i][j])
			result = checkRow(row)
			if result == 'X' or result == 'O':
				break;
			elif result == '.':
				hasBlank = 1

	if result != 'X' and result != 'O':
		# check diagonal1
		row = []
		for i in range(4):
			row.append(table[i][i])
		result = checkRow(row)
		if result == '.':
			hasBlank = 1

	if result != 'X' and result != 'O':
		# check diagonal2
		row = []
		for i in range(4):
			row.append(table[i][3 - i])
		result = checkRow(row)
		if result == '.':
			hasBlank = 1

	if result == 'X':
		result = 'X won'
	elif result == 'O':
		result = 'O won'
	elif hasBlank:
		result = 'Game has not completed'
	else:
		result = 'Draw'

	print ("Case #%d: %s" % (t + 1, result))