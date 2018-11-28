t = int(input())

def resetcount():
	return [0,0,0,0]

def chartype(char,counts):
	if char=='X':
		counts[0]+=1
	if char=='O':
		counts[1]+=1
	if char=='.':
		counts[2]+=1
	if char=='T':
		counts[3]+=1
	return

def vict(count):
	if (count[0]==4) or (count[0]==3 and count[3]==1) :
		res = 1
		return res
	if (count[1]==4) or (count[1]==3 and count[3]==1) :
		res = 2
		return res
	return 0

def analyze(board):
	#Case 1 Analyze the rows
	res = 0
	nodot =0
	counts = [0,0,0,0]
	for rows in board:
		for char in rows:
			chartype(char,counts)
		a = vict(counts)
		if (a==1) or (a==2):
			counts=resetcount()
			return a
		if counts[2]==0:
			nodot+=1
		counts=resetcount()
	for cols in xrange(len(board)):
		for char in xrange(len(board)):
			chartype(board[char][cols],counts)
		a = vict(counts)
		if (a==1) or (a==2):
			counts=resetcount()
			return a
		counts=resetcount()
	for cols in xrange(len(board)):
		chartype(board[cols][cols],counts)
	a = vict(counts)
	if (a==1) or (a==2):
		counts=resetcount()
		return a
	counts=resetcount()
	for cols in xrange(len(board)):
		chartype(board[cols][3-cols],counts)
	a = vict(counts)
	if (a==1) or (a==2):
		counts=resetcount()
		return a
	counts=resetcount()
	if nodot==4:
		return 3
	return 0

for i in xrange(t):
	board = []
	for j in range(4):
		board.append(raw_input())
	a=raw_input()
	res = analyze(board)
	if res==3:
		print "Case #%d: Draw" %(i+1)
	if res==1:
		print "Case #%d: X won" %(i+1)
	if res==2:
		print "Case #%d: O won" %(i+1)
	if res==0:
		print "Case #%d: Game has not completed" %(i+1)







		




