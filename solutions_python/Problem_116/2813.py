

T = int(raw_input())
count = 0

for _ in range(T):
	m = []
	for c in range(4):
		m.append(raw_input())
	#print m

	xwon = False
	owon = False
	notover = False
	#horizontal
	for i in range(4):
		c = m[i][0]
		if c == 'T':
			c = m[i][1]
		for j in range(4):
			if m[i][j] == '.':
				notover = True
				break
			if c != m[i][j] and m[i][j] != 'T':
				break
		else:
			if c == 'X':
				xwon = True
			else:
				owon = True
			break
	
	if not (xwon or owon):
		for i in range(4):
			c = m[0][i]
			if c == 'T':
				c = m[1][i]
			for j in range(4):
				if m[j][i] == '.' or c != m[j][i] and m[j][i] != 'T':
					break
			else:
				if c == 'X':
					xwon = True
				else:
					owon = True
				break
	#diagonals
	if not (xwon or owon):
		c = m[0][0]
		if c == 'T':
			c = m[1][1]
		for i in range(4):
			if m[i][i] == '.' or c != m[i][i] and m[i][i] != 'T':
				break
		else:
			if c == 'X':
				xwon = True
			else:
				owon = True
		c = m[0][3]
		if c == 'T':
			c = m[1][2]
		for i in range(4):
			if m[i][3-i] == '.' or c != m[i][3-i] and m[i][3-i] != 'T':
				break
		else:
			if c == 'X':
				xwon = True
			else:
				owon = True




	count += 1
	print 'Case #'+str(count)+':',
	if xwon:
		print 'X won'
	if owon:
		print 'O won'
	if (not (xwon or owon)) and notover:
		print 'Game has not completed'
	elif not (xwon or owon):
		print 'Draw'
	T -= 1
	raw_input() #discard last line
