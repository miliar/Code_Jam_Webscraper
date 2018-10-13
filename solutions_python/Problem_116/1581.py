
def solve(l1,l2,l3,l4,caseNum):
	board = [l1,l2,l3,l4]
	for i in range(4):
		x = len([x for x in board[i] if x in ['X','T']])
		if x == 4:
			printWin(caseNum,'X')
			return
		o = len([x for x in board[i] if x in ['O','T']])
		if o == 4:
			printWin(caseNum,'O')
			return

	for j in range(4):
		c = []
		for i in range(4):
			c.append(board[i][j])
		x = len([x for x in c if x in ['X','T']])
		if x == 4:
			printWin(caseNum,'X')
			return
		o = len([x for x in c if x in ['O','T']])
		if o == 4:
			printWin(caseNum,'O')
			return
	d = []
	dd = []
	for j in range(4):
		d.append(board[j][j])
		dd.append(board[j][3-j])

	x = len([x for x in d if x in ['X','T']])
	xx = len([x for x in dd if x in ['X','T']])
	if x == 4 or xx == 4:
		printWin(caseNum,'X')
		return

	o = len([x for x in d if x in ['O','T']])
	oo = len([x for x in dd if x in ['O','T']])
	if o == 4 or oo == 4:
		printWin(caseNum,'O')
		return

	for i in range(4):
		dot = [x for x in board[i] if x =='.']
		if dot:
			of.write('Case #'+ str(caseNum) + ': '+'Game has not completed' +'\n')
			print 'Case #'+ str(caseNum) + ': '+ "Game has not completed"
			return
	
	of.write('Case #'+ str(caseNum) + ': '+'Draw' +'\n')
	print 'Case #'+ str(caseNum) + ': '+ "Draw"
	
def printWin(caseNum, winner):
	of.write('Case #'+ str(caseNum) + ': '+ winner +" won" +'\n')
	print 'Case #'+ str(caseNum) + ': ' +winner +" won"

ar = 1
if ar == 1:
	f = open('A-small-practice.in', 'r')
else:
	f = open('C-large-practice.in', 'r')
of = open('out.txt','w')
lines = f.read().splitlines()
cases = int(lines[0])
for i in range(1,cases+1):
	solve(lines[(i*5)-4],lines[(i*5)-3],lines[(i*5)-2],lines[(i*5)-1],i)
f.close()
of.close()