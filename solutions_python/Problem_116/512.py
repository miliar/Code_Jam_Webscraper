T = input()
f = open("A.out", 'w')
for z in range(T):	
	board = []
	for i in range(4):
		s = raw_input()
		board.append(s)
	#print board[0][3]
	raw_input()
	completed = True
	Owins = False
	Xwins = False
	#Horizontal wins

	for i in range(4):
		same = True
		for o in range(4):
			if board[i][o] != 'O' and board[i][o] != 'T':
				same = False
			if board[i][o] == '.':
				completed = False
		if same:
			Owins = True

	for i in range(4):
		same = True
		for o in range(4):
			if board[o][i] != 'O' and board[o][i] != 'T':
				same = False
		if same:
			Owins = True

	same = True
	for i in range(4):
		if board[i][i] != 'O' and board[i][i] != 'T':
			same = False
	if same:
		Owins = True

	same = True
	for i in range(4):
		if board[3-i][i] != 'O' and board[3-i][i] != 'T':
			same = False
	if same:
		Owins = True


	for i in range(4):
		same = True
		for o in range(4):
			if board[i][o] != 'X' and board[i][o] != 'T':
				same = False
		if same:
			Xwins = True

	for i in range(4):
		same = True
		for o in range(4):
			if board[o][i] != 'X' and board[o][i] != 'T':
				same = False
		if same:
			Xwins = True

	same = True
	for i in range(4):
		if board[i][i] != 'X' and board[i][i] != 'T':
			same = False
	if same:
		Xwins = True

	same = True
	for i in range(4):
		if board[3-i][i] != 'X' and board[3-i][i] != 'T':
			same = False
	if same:
		Xwins = True	

	if Owins:
		f.write("Case #"+str(z+1)+": O won\n")
	elif Xwins:
		f.write("Case #"+str(z+1)+": X won\n")
	elif completed:
		f.write("Case #"+str(z+1)+": Draw\n")
	else:
		f.write("Case #"+str(z+1)+": Game has not completed\n")
