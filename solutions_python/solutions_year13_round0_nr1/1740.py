import sys
  
N = sys.stdin.readline()

for case in range(0,int(N)):
	status_X = []
	status_X.append([0 for x in range(0,4)]) # Row
	status_X.append([0 for x in range(0,4)]) # Cell
	status_X.append([0 for x in range(0,4)]) # D
	status_O = []
	status_O.append([0 for x in range(0,4)])
	status_O.append([0 for x in range(0,4)])
	status_O.append([0 for x in range(0,4)])
	empty = False

	for x in range(0,4):
		line = sys.stdin.readline()
		for y in range(0,4):
			c = line[y]
			if c=='X' or c=='T':
				status_X[0][x]+=1
				status_X[1][y]+=1
			if c=='O' or c=='T':
				status_O[0][x]+=1
				status_O[1][y]+=1
			if c=='.':
				empty = True

			if x==y:
				if c=='X' or c=='T':
					status_X[2][0]+=1
				if c=='O' or c=='T':
					status_O[2][0]+=1

			if 3-x==y:
				if c=='X' or c=='T':
					status_X[2][1]+=1
				if c=='O' or c=='T':
					status_O[2][1]+=1

	win_X = False
	for status in status_X:
		for v in status:
			if v==4: 
				win_X = True
	win_O = False
	for status in status_O:
		for v in status:
			if v==4: 
				win_O = True
	
	res = "Game has not completed"
	if win_X:
		res = "X won"
	elif win_O:
		res = "O won"
	elif not empty:
		res = "Draw"
	
	sys.stdin.readline() #Empty line

	print "Case #%d: %s" % (case+1, res)
