import sys

T = int(sys.stdin.readline());

board = []
caseNum = 1;
for t in range(T):

	# get lawn size
	YX = sys.stdin.readline().strip().split(' ')
	Y = int(YX[0])
	X = int(YX[1])

	# get lawn
	lawn = []
	for y in range(Y):
		row = [int(cell) for cell in sys.stdin.readline().strip().split()]
		lawn.append(row)

	# can do the n^2 solution since input is small

	lawnCondition = True

	for y in range(Y):
		for x in range(X):
			# get the lists for each condition
			below = [lawn[y][x] for y in range(y + 1)]
			above = [lawn[y][x] for y in range(y,Y)]
			left = [lawn[y][x] for x in range(x + 1)]
			right = [lawn[y][x] for x in range(x,X)]

			cell = lawn[y][x]

			cellCondition = (cell >= max(below) and cell >= max(above)) or (cell >= max(left) and cell >= max(right))
			lawnCondition = lawnCondition and cellCondition
			if not lawnCondition:
				break
		if not lawnCondition:
			break

	print('Case #' + str(t+1) + ': ', end='')

	if lawnCondition:
		print('YES')
	else:
		print('NO')