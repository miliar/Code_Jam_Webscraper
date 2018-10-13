def checkWin(arr, idx):
	chars = ["X", "O"]
	for c in chars:
		good = True
		for i in xrange(4):
			if arr[idx][i] != c and arr[idx][i] != 'T':
				good = False
				break
		if good:
			return True, c
		good = True
		for i in xrange(4):
			if arr[i][idx] != c and arr[i][idx] != 'T':
				good = False
				break
		if good:
			return True, c
	return False, "_"
	
def checkWinDiagonal(arr):
	chars = ["X", "O"]
	for c in chars:
		good = True
		for i in xrange(4):
			if arr[i][i] != c and arr[i][i] != 'T':
				good = False
				break
		if good:
			return True, c
		good = True
		for i in xrange(4):
			if arr[i][3-i] != c and arr[i][3-i] != 'T':
				good = False
				break
		if good:
			return True, c
	return False, "_"
	
def checkFilled(arr):
	good = True
	for i in xrange(4):
		for j in xrange(4):
			if arr[i][j] == '.':
				good = False
				break
	return good
	
f = open("tomek.in")

c = int(f.readline().strip())
for i in xrange(c):
	data = []
	for j in xrange(4):
		data.append([char for char in f.readline().strip()])
	f.readline() #eat up the last line
	
	won = False
	winner = 0
	#check if somebody had won
	#horizontal and vertical
	for j in xrange(4):
		won, winner = checkWin(data, j)
		if won:
			break
	#check diagonal
	if not won:
		won, winner = checkWinDiagonal(data)
	
	if won:
		#print winner
		print "Case #"+str(i+1)+": "+winner+" won"
	else:
		#check if all squares are filled
		filled = checkFilled(data)
		if filled:
			#Draw
			print "Case #"+str(i+1)+": Draw"
		else:
			#Not completed
			print "Case #"+str(i+1)+": Game has not completed"
f.close()