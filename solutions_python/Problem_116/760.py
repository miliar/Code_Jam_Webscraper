def hasWon(board,player):
	for x in range(4):
		states=[]
		for y in range(4):
			states.append(board[x][y])
		for i in states:
			if i!=player and i!='T':
				break
		else:
			return True
	for y in range(4):
		states=[]
		for x in range(4):
			states.append(board[x][y])
		for i in states:
			if i!=player and i!='T':
				break
		else:
			return True
	states=[]
	for i in range(4):
		states.append(board[i][i])
	for i in states:
		if i!=player and i!='T':
			break
	else:
		return True
	states=[]
	for i in range(4):
		states.append(board[len(board)-1-i][i])
	for i in states:
		if i!=player and i!='T':
			break
	else:
		return True
	return False
def determineState(board):
	if hasWon(board,'X'):
		return 'X won'
	if hasWon(board,'O'):
		return 'O won'
	for i in board:
		if '.' in i:
			break
	else:
		return 'Draw'
	return 'Game has not completed'
lines=open('A-large.in','r').readlines()[1:]
for i in range(len(lines)):
	lines[i]=lines[i].replace('\n','')
out=open('large_output.txt','w')
curCase=1
for i in range(0,len(lines),5):
	board=[[]]*4
	for j in range(4):
		board[j]=[q for q in lines[i+j]]
	out.write(('Case #{0}: '+determineState(board)+'\n').format(curCase))
	curCase+=1