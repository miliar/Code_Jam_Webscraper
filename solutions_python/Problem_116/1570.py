import sys

def getWinner(value,t,a):
	Winner = None
	if value >=3 or value <=-3:
		if value == 4 or (value == 3 and t == a):
			Winner = "X"
		elif value == -4 or (value == -3 and t == a):
			Winner = "O"
	return Winner

def diagonalTest(value,ta,tb):
	Winner = None
	if (ta is None):
		Winner = getWinner(value,-1,1)
	else:
		Winner = getWinner(value,ta+tb,3)
	return Winner



my_file = open(sys.argv[1], 'r')

tests = int(my_file.readline())
for i in range(tests):
	matrix = []
	for j in range(4):
		tx = (my_file.readline()).rstrip('\n')
		matrix.append(list(tx))
	ta = None
	tb = None
	dots = 0
	c = [0,0,0,0]
	d1 = 0
	d2 = 0
	Winner = None
	a = 0
	lines_to_read = 5
	message = "Game has not completed"
	#print matrix
	for a in range(4):
		lines_to_read -=1
		line = 0
		for b in range(4):
			if matrix[a][b] == ".":
				dots+=1
			elif matrix[a][b] == "X":
				line +=1
				c[b] +=1
			elif matrix[a][b] == "O":
				line -=1
				c[b] -=1
			elif matrix[a][b] == "T":
				ta=a
				tb=b
			else:
				exit(0)
			if a == b:
				if matrix[a][b] == "X":
					d1+=1
				if matrix[a][b] == "O":
					d1-=1
			if a + b == 3:
				if matrix[a][b] == "X":
					d2+=1
				if matrix[a][b] == "O":
					d2-=1
		Winner = getWinner(line,ta,a)
		if Winner is not None:
			message = Winner+" won"
			#print  "line {0} {1}".format(a,message)
			break
	if Winner is None:
		for b in range(4):
			#print "try c{0}".format(b)
			Winner = getWinner(c[b],tb,b)
			if Winner is not None:
				message = Winner+" won"
				#print  "col {0} {1}".format(b,message)
				break	
	if Winner is None:
		Winner = diagonalTest(d1,ta,tb)
		if Winner is not None:
			message = Winner+" won"
		else:
			Winner = diagonalTest(d2,ta,tb)
			if Winner is not None:
				message = Winner+" won"
	if Winner is None:
		if dots == 0:
			message = "Draw"
	print "Case #{0}: {1}".format((i+1),message)
	tx = my_file.readline()
	#print tx
