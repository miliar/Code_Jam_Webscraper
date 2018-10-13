import sys
input = sys.stdin.readlines()

def GCD(x, y):
	if x + y > 0 :
		g = y
		while x > 0:
			g = x
			x = y % x
			y = g
		return g
	else:
		return 0

def div(a,b):
	if a == b == 0: return 'undef'
	elif b == 0: return 'inf'
	else: return float(a)/float(b)


T = int(input[0][:len(input[0])-1])
inpLine = 1
for t in range(1, T+1):
	Tcase = input[inpLine]
	if input[inpLine][len(input[inpLine])-1] == '\n':
		Tcase = input[inpLine][:len(input[inpLine])-1]
	Tcase = Tcase.split(' ')
	H = int(Tcase[0])
	W = int(Tcase[1])
	D = int(Tcase[2])

	grid = input[inpLine+1:inpLine+H+1]
	for j in range(0,len(grid)):
		grid[j] = grid[j][:W]
	inpLine += (H+1)

	for i in range(0,H):
		for j in range(0,W):
			if grid[i][j] == 'X':
				Mypos = (i,j)

	topDist = Mypos[0]-0.5
	bottomDist = H-Mypos[0]-1.5
	leftDist = Mypos[1]-0.5
	rightDist = W-Mypos[1]-1.5

	HorImagePos = [(0,0,' ')]
	dist = 0
	z = 1
	while dist <= D:
		if z%2==0:
			if (dist+2*(rightDist) <= D):
				HorImagePos.append((dist+2*(rightDist),z,'l'))
			dist += 2*(rightDist)
		else:
			if (dist+2*(leftDist) <= D):
				HorImagePos.append((dist+2*(leftDist),z,'l'))
			dist += 2*(leftDist)
		z += 1

	dist = 0
	z = 1
	while dist <= D:
		if z%2==1:
			if (dist+2*(rightDist) <= D):
				HorImagePos.append((dist+2*(rightDist),z,'r'))
			dist += 2*(rightDist)
		else:
			if (dist+2*(leftDist) <= D):
				HorImagePos.append((dist+2*(leftDist),z,'r'))
			dist += 2*(leftDist)
		z += 1

	VerImagePos = [(0,0,' ')]
	dist = 0
	z = 1
	while dist <= D:
		if z%2==0:
			if (dist+2*(topDist) <= D):
				VerImagePos.append((dist+2*(topDist),z,'b'))
			dist += 2*(topDist)
		else:
			if (dist+2*(bottomDist) <= D):
				VerImagePos.append((dist+2*(bottomDist),z,'b'))
			dist += 2*(bottomDist)
		z += 1

	dist = 0
	z = 1
	while dist <= D:
		if z%2==1:
			if (dist+2*(topDist) <= D):
				VerImagePos.append((dist+2*(topDist),z,'t'))
			dist += 2*(topDist)
		else:
			if (dist+2*(bottomDist) <= D):
				VerImagePos.append((dist+2*(bottomDist),z,'t'))
			dist += 2*(bottomDist)
		z += 1
	HorImagePos = sorted(HorImagePos)
	VerImagePos = sorted(VerImagePos)

	count = 0
	lightDirs = [('undef',' ',' ')]
	for i in HorImagePos:
		for j in VerImagePos:
			if (((i[0]*i[0]) + (j[0]*j[0])) <= (D*D)):
#				if GCD(i[1],j[1]) == 1:
				if (div(i[0],j[0]), i[2], j[2]) not in lightDirs:
					count += 1
					lightDirs.append((div(i[0],j[0]), i[2], j[2]))
			else:
				break

	print 'Case #' + str(t) + ': ' + str(count)
