f = open('A-large.in.txt','r')
g = open('output.txt', 'w')
C = int(f.readline())

for i in range(C):
	r = []
	solved = 0
	unfin = 0
	for j in range(4):
		r.append([])
		hold = f.readline().strip()
		if solved == 0:
			for k in range(4):
				if hold[k] == 'X':
					r[j].append(1)
				elif hold[k] == 'O':
					r[j].append(2)
				elif hold[k] == 'T':
					r[j].append(3)
				else:
					r[j].append(0)
					unfin = 1
			horcheck = r[j][0] * r[j][1] * r[j][2] * r[j][3]
			if horcheck == 1 or horcheck == 3:
				g.write('Case #%d: X won\n' % (i+1))
				solved = 1
			elif horcheck == 16 or horcheck == 24:
				g.write('Case #%d: O won\n' % (i+1))
				solved = 1
	temp = f.readline().strip()
	
	if solved == 0:
		for j in range(4):
			vercheck = r[0][j] * r[1][j] * r[2][j] * r[3][j]
			if vercheck == 1 or vercheck == 3:
				g.write('Case #%d: X won\n' % (i+1))
				solved = 1
			elif vercheck == 16 or  vercheck == 24:
				g.write('Case #%d: O won\n' % (i+1))
				solved = 1
	
	if solved == 0:
		diagcheck1 = r[0][0] * r[1][1] * r[2][2] * r[3][3]
		if diagcheck1 == 1 or diagcheck1 == 3:
			g.write('Case #%d: X won\n' % (i+1))
			solved = 1
		elif diagcheck1 == 16 or diagcheck1 == 24:
			g.write('Case #%d: O won\n' % (i+1))
			solved = 1

		diagcheck2 = r[0][3] * r[1][2] * r[2][1] * r[3][0]
		if diagcheck2 == 1 or diagcheck2 == 3:
			g.write('Case #%d: X won\n' % (i+1))
			solved = 1
		elif diagcheck2 == 16 or diagcheck2 == 24:
			g.write('Case #%d: O won\n' % (i+1))
			solved = 1
	
	if solved == 0:
		if unfin == 0:
			g.write('Case #%d: Draw\n' % (i+1))
		else:
			g.write('Case #%d: Game has not completed\n' % (i+1))
	