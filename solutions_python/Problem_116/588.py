from time import time

def nextCase():
	fileName = "A-large.in"
	n = None
	T = [[None for i in range(4)] for j in range(4)]
	for line in open(fileName, 'r').readlines():
		if None == n: n, i = int(line), 0
		elif None == i: i = 0
		elif 4 != i: 
			for j in range(4):
				T[i][j] = line[j]
			i += 1
		else:
			i = 0
			yield T



def solve(T):
	def checkWin(C):
		for i in range(4):
			flag = True
			for j in range(4):
				if C != T[i][j] and 'T' != T[i][j]: flag = False
			if flag: return True
		for i in range(4):
			flag = True
			for j in range(4):
				if C != T[j][i] and 'T' != T[j][i]: flag = False
			if flag: return True

		flag = True
		for i in range(4):
			if C != T[i][i] and 'T' != T[i][i]: flag = False
		if flag: return True

		flag = True
		for i in range(4):
			if C != T[i][3 - i] and 'T' != T[i][3 - i]: flag = False
		if flag: return True

		return False

	def checkGameIsOver():
		for i in range(4):
			for j in range(4):
				if '.' == T[i][j]: return False
		return True

	if checkWin('X'): return "X won"
	if checkWin('O'): return "O won"
				
	return "Draw" if checkGameIsOver() else "Game has not completed"

start = time()

i = 1
for T in nextCase():
	print("Case #%d: %s" % (i, solve(T)))
	i += 1


#print(time() - start)
