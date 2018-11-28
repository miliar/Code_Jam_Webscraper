# code by gabirobs, always having fun ^^
		 
def removeT(case):
	return case[:case.find('T')] + case[case.find('T')+1:]
	
def status(game):
	diagonal1 = ''
	for i in range(4):
		diagonal1 += game[i][i]
	if diagonal1 == 'XXXX':
		return 'X won'
	if diagonal1 == 'OOOO':
		return 'O won'
	if 'T' in diagonal1:
		if removeT(diagonal1) == 'XXX':
			return 'X won'
		if removeT(diagonal1) == 'OOO':
			return 'O won'
	
	diagonal2 = ''
	for i in range(4):
		diagonal2 += game[i][-(i+1)]
	if diagonal2 == 'XXXX':
		return 'X won'
	if diagonal2 == 'OOOO':
		return 'O won'
	if 'T' in diagonal2:
		if removeT(diagonal2) == 'XXX':
			return 'X won'
		if removeT(diagonal2) == 'OOO':
			return 'O won'
			
	for i in range(4):
		line = ''
		for k in range(4):
			line += game[i][k]
		if line == 'XXXX':
			return 'X won'
		if line == 'OOOO':
			return 'O won'
		if 'T' in line:
			if removeT(line) == 'XXX':
				return 'X won'
			if removeT(line) == 'OOO':
				return 'O won'
			
	for i in range(4):
		column = ''	
		for k in range(4):
			column += game[k][i]
		if column == 'XXXX':
			return 'X won'
		if column == 'OOOO':
			return 'O won'
		if 'T' in column:
			if removeT(column) == 'XXX':
				return 'X won'
			if removeT(column) == 'OOO':
				return 'O won'
	
	for i in range(4):
		if '.' in game[i]:
			return 'Game has not completed'
	
	return 'Draw'
	
file = open("A-large.in", "r")
T = int(file.readline())

output = open("A-large.out", "w")

for i in range(T):
	board = []
	for k in range(4):
		board.append(file.readline().strip('\n'))
	jump = file.readline()
	output.write('Case #%d: %s\n' %(i+1, status(board)))