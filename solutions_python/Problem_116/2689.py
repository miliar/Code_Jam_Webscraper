import sys

f = open(sys.argv[1], 'r')
T = int(f.readline())
r = open(sys.argv[2], 'w')


mat= [[0 for i in range(4)] for j in range(4)]

def solve(mat):
	game_completed = True
	for i in range(0,4):
		for j in range(0,4):
			if mat[i][j] == '.':
				game_completed = False
				continue
			if (wonRow(mat[i][j],mat,i) or wonColumn(mat[i][j],mat,j)):
				return mat[i][j] + " won"
			if (i == 0 and j ==0 and wonFirstDiag(mat[i][j],mat)):
				return mat[i][j] + " won"
			if (i == 0 and j ==3 and wonLastDiag(mat[i][j],mat)):
				return mat[i][j] + " won"
	if game_completed:
		return "Draw"
	return "Game has not completed"

def wonRow(s,mat,row):
	for j in range(0,4):
		if s != mat[row][j] and mat[row][j] !='T':
			return False
	return True

def wonColumn(s,mat,column):
	for i in range(0,4):
		if s != mat[i][column] and mat[i][column] != 'T':
			return False
	return True

def wonFirstDiag(s,mat):
	for i in range(0,4):
		if s != mat[i][i] and mat[i][i] != 'T':
			return False
	return True

def wonLastDiag(s,mat):
	i = 0
	j = 3
	while j >= 0:
		if s != mat[i][j] and mat[i][j] != 'T':
			return False
		j = j -1
		i = i + 1
	return True

for case in range(0,T):
	for i in range(0,4):
		line = f.readline().strip()
		#print line
		j = 0
		for c in line:
			mat[i][j] = c
			j = j + 1
	line =f.readline()
	r.write("Case #"+str(case+1)+": " + solve(mat)+'\n')


