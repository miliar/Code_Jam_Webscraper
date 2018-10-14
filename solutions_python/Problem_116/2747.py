from collections import Counter

f=open('A-small-attempt1.in','r+')
testcases=int(f.readline())

def checkboard(board):
	for i in range(0,4):
		#Check Line
		a=board[i]
		c=Counter(a)
		#Check Unfinished
		unfinished=False
		if c['.'] != 0:
			unfinished=True
		if c['X'] + c['T'] == 4 :
			return 'X'
		if c['O'] + c['T'] == 4 :
			return 'O'
		#Check Col
		a =[row[i] for row in board]
		c=Counter(a)
		if c['X'] + c['T'] == 4 :
			return 'X'
		if c['O'] + c['T'] == 4 :
			return 'O'
		#Check Diag L->R
		a=board[0][0],board[1][1],board[2][2],board[3][3]
		c=Counter(a)
		if c['X'] + c['T'] == 4 :
			return 'X'
		if c['O'] + c['T'] == 4 :
			return 'O'
		#Check Diag L->R
		a=board[0][3],board[1][2],board[2][1],board[3][0]
		c=Counter(a)
		if c['X'] + c['T'] == 4 :
			return 'X'
		if c['O'] + c['T'] == 4 :
			return 'O'
	else:
		if unfinished :
			return 'unfinisehd'
		return 'draw'
for i in range(1,testcases+1):
	board = [[0 for x in xrange(4)] for x in xrange(4)] 
	for j in range(0,4):
		s=f.readline()
		for h in range(0,4):
			board[j][h]=s[h]
	f.readline()
	winner=checkboard(board)
	if winner == 'unfinisehd':
		print "Case #" + str(i) + ": Game has not completed"
	elif winner == 'draw':
		print "Case #" + str(i) + ": Draw"
	else:
		print "Case #" + str(i) + ": " +  winner +" won"
	
	