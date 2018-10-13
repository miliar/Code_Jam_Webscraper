fp = open("text1.txt", "w")
pf = open("A-large.in", "r")

xWin1 = ['T','X','X','X']
xWin2 = ['X','X','X','X']
oWin1 = ['O','O','O','T']
oWin2 = ['O','O','O','O']

def controlRow(matrix):
	for i in range(0,4):
		if sorted(matrix[i]) == xWin1 or sorted(matrix[i]) == xWin2:
			return 1
		if sorted(matrix[i]) == oWin1 or sorted(matrix[i]) == oWin2:
			return 2
	return 0

def controlCol(matrix):
	for i in range(0,4):
		l = [matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i]]
		if sorted(l) == xWin1 or sorted(l) == xWin2:
			return 1
		if sorted(l) == oWin1 or sorted(l) == oWin2:
			return 2
	return 0

def controlDiag(matrix):
	d1, d2 = [], []
	for i in range(0,4):
		d1.append(matrix[i][i])
		d2.append(matrix[i][3-i])
	for i in range(0,4):
		if sorted(d1) == xWin1 or sorted(d1) == xWin2 or sorted(d2) == xWin1 or sorted(d2) == xWin2:
			return 1
		if sorted(d1) == oWin1 or sorted(d1) == oWin2 or sorted(d2) == oWin1 or sorted(d2) == oWin2:
			return 2
	return 0

def lookForPoints(matrix):
	for i in range(0,4):
		for j in range(0,4):	
			if matrix[i][j] == '.':
				return True
	return False


def write():
	t = int(pf.readline())
	for i in range(0, t):
		x = i + 1
		matrix = []
		for j in range(0,4):
			s = pf.readline()
			row = [s[0], s[1], s[2], s[3]]
			matrix.append(row)
		print matrix
		pf.readline()
		
		if controlRow(matrix) == 1 or controlCol(matrix) == 1 or controlDiag(matrix) == 1:
			fp.write("Case #"+str(x)+": X won")
		elif controlRow(matrix) == 2 or controlCol(matrix) == 2 or controlDiag(matrix) == 2:
			fp.write("Case #"+str(x)+": O won")
		elif lookForPoints(matrix):
			fp.write("Case #"+str(x)+": Game has not completed")
		else:
			fp.write("Case #"+str(x)+": Draw")
		fp.write("\n")
	
write()

