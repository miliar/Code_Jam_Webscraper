t = raw_input()
t = int(t)
X = 'XXXX'
O = 'OOOO'
for i in range(0,t):
    winner='D'
    draw=1
    board = []
    for j in range (0,4):
	board.append(raw_input())
	if board[j].find('.')!=-1: draw=0
    for j in range (0,4):
	if board[j].replace('T','X')==X: winner='X'
	if board[j].replace('T','O')==O: winner='O'
    for j in range (0,4):
	s=[]
	for k in range (0,4):
	    s.append(board[k][j])
	s=("".join(s))
	if s.replace('T','X')==X: winner='X'
	if s.replace('T','O')==O: winner='O'
    s=[]
    for j in range (0,4):
	s.append(board[j][j])
    s=("".join(s))
    if(s.replace('T','X')==X): winner='X'
    if(s.replace('T','O')==O): winner='O'
    s=[]
    for j in range (0,4):
	s.append(board[j][3-j])
    s=("".join(s))
    if(s.replace('T','X')==X): winner='X'
    if(s.replace('T','O')==O): winner='O'
    if winner=='X':
	print "Case #{}: X won".format(i+1)
    elif winner=='O':
	print "Case #{}: O won".format(i+1)
    elif winner=='D' and draw==1:
	print "Case #{}: Draw".format(i+1)
    else:
	print "Case #{}: Game has not completed".format(i+1)
    s=raw_input()

