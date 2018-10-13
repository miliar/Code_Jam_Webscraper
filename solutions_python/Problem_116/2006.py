f = open('test.txt', "r")

num = f.readline()

x = []
o = []

ff = True

cases = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15], [0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15], [0,5,10,15], [3,6,9,12]]

for i in range(int(num)):
	board = []
	for j in range(4):
		board.append(f.readline())

	for xx in range(4):
		for yy in range(4):
			if board[xx][yy] is "X":
				x.append(yy+xx*4)

			if board[xx][yy] is "O":
				o.append(yy+xx*4)

			if board[xx][yy] is "T":
				x.append(yy+xx*4)
				o.append(yy+xx*4)

			if board[xx][yy] is ".":
				ff = False



	for case in cases:
		if set(case).issubset(set(x)):
			print "Case #" + str(i+1) + ": X won"
			break
		if set(case).issubset(set(o)):
			print "Case #" + str(i+1) + ": O won"
			break
		if ff and all(a in case for a in [3,6,9,12]):
			print "Case #" + str(i+1) + ": Draw"
			break
		if all(a in case for a in [3,6,9,12]):
			print "Case #" + str(i+1) + ": Game has not completed"

	f.readline()
	x = []
	o = []
	ff = True






f.close()











