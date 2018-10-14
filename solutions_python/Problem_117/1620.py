f = open('B-small-attempt9.in')
f=f.read().splitlines()
cases = int(f[0]) # number of cases in the file

f = [ map(int, x.split()) for x in f] # list of list of ints

ans=""
case = 0
line = 1

def printB(b):
	for i in range(len(b)):
		print b[i]

def flip(board):
	b2 = [ x[:] for x in board]
	for col in range(M): # check first row
		perp = [board[num][col] for num in range(N)]
		if sum(perp) == N: #if row of 1, replace with opposite
			for row in range(N):
				b2[row][col] = 2
	for row in range(N): # check row
		if sum(board[row]) == M:
			b2[row] = [2 for z in range(M)]
	printB(b2)
	if sum([sum(b2[row]) for row in range(N)]) == N*M*2:
		return True
	else:
		return False


for i in range(cases): 
	case += 1
	N = f[line][0]
	M = f[line][1]
	board = [f[line+x] for x in range(1,N+1) ]
	printB(board)
	print "-----"
	if flip(board):
		ans += "Case #" + str(case) +": YES\n"
		print "YES"
	else:
		ans += "Case #" + str(case) +": NO\n"
		print "NO"
	line += N + 1 # move to next case
a=open('answerSmall.txt','w')
a.write(ans)
