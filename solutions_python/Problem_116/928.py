f = open('input.txt');
lines = f.read().split('\n');

nb = int(lines[0])

linesX = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
linesY = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']

def checkTTT(m):
	#columns
	for x in range(0, 4):
		l = m[0][x] + m[1][x] + m[2][x] + m[3][x]
		if l in linesX:
			return 'X'
		if l in linesY:
			return 'O'
	#diagonales
	l = m[0][0] + m[1][1] + m[2][2] + m[3][3]
	if l in linesX:
		return 'X'
	if l in linesY:
		return 'O'
	
	l = m[0][3] + m[1][2] + m[2][1] + m[3][0]
	if l in linesX:
		return 'X'
	if l in linesY:
		return 'O'
	
	return ''
			
for i in range(0, nb):
	m = [ ['' for x in range(0, 4)] for y in range(0, 4)]
	winnerX = False
	winnerY = False
	draw = True
	
	for x in range(0, 4):
		l = lines[1 + i*5 + x]
		
		if l in linesX:
			winnerX = True
		if l in linesY:
			winnerY = True
			
		for y in range(0, 4):
			if l[y] == '.':
				draw = False
			m[x][y] = l[y]
	
	if winnerX:
		print "Case #%s: X won" % (i+1)
	elif winnerY:
		print "Case #%s: O won" % (i+1)
	else:
		t = checkTTT(m)
		if len(t) > 0:
			print "Case #%s: %s won" % (i+1, t)
		else:
			if draw:
				print "Case #%s: Draw" % (i+1)
			else:
				print "Case #%s: Game has not completed" % (i+1)
		