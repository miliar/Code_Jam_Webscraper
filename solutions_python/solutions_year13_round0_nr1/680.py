def solve(a):
	d1x = 0
	d1o = 0
	d2x = 0
	d2o = 0

	for i in range(4):
		hx = 0
		ho = 0
		for j in range(4):
			if(a[i][j] == 'X'):
				hx += 1
			elif(a[i][j] == 'O'):
				ho += 1
			elif(a[i][j] == 'T'):
				hx += 1
				ho += 1

		vx = 0
		vo = 0
		for j in range(4):
			if(a[j][i] == 'X'):
				vx += 1
			elif(a[j][i] == 'O'):
				vo += 1
			elif(a[j][i] == 'T'):
				vx += 1
				vo += 1		

		if(hx == 4 or vx == 4):
			return "X won"
		if(ho == 4 or vo == 4):
			return "O won"

		if(a[i][i] == 'X'):
			d1x += 1
		elif(a[i][i] == 'O'):
			d1o += 1
		elif(a[i][i] == 'T'):
			d1x += 1
			d1o += 1

		if(a[i][3 - i] == 'X'):
			d2x += 1
		elif(a[i][3 - i] == 'O'):
			d2o += 1
		elif(a[i][3 - i] == 'T'):
			d2x += 1
			d2o += 1
 

	if(d1x == 4 or d2x == 4):
		return "X won"
	if(d1o == 4 or d2o == 4):
		return "O won"

	for i in range(4):
		for j in range(4):
			if(a[i][j] == '.'):
				return "Game has not completed"
			
	return "Draw"

T = input()
a = []
for i in range(T):
	a = []
	for j in range(4):
		a.append(raw_input())
	raw_input()
	print "Case #" + str(i + 1) + ": " + solve(a)
