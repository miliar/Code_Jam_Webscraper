__author__ = 'Artur'

def red(m, i, j, r, c):
	res = True
	if not (m[i][j] == '#'):
		res = False
	if not ( (i + 1 < r and j < c) and  m[i + 1][j] == '#' ):
		res = False
	if  not ( (i < r and j + 1 < c) and m[i][j + 1] == '#' ):
		res = False
	if not ( (i + 1 < r and j + 1 < c) and  m[i+1][j+1] == '#' ):
		res = False
	return res

def makeRed(m, i, j):
	m[i][j] = '/'
	m[i + 1][j] = '\\'
	m[i][j + 1] = '\\'
	m[i+1][j+1] = '/'

T = int ( raw_input() )

for t in range(1, T + 1):

	m = []
	
	l = [int(x) for x in raw_input().split() ]
	r = l[0]
	c = l[1]
	
	for i in range(0, r):
		x = raw_input()
		y = [ i for i in x ] 
		m.append ( y )
		
	for i in range (0, r):
		for j in range (0, c):
			if red(m, i, j, r, c):
				makeRed(m, i, j)
	
	pos = True
	for i in range (0, r):
		for j in range(0, c):
			if m[i][j] == '#':
				pos = False
				break;
				
	if pos:
		print "Case #%d:" % t
		for r in m:
			l = ""
			for c in r:
				l += c
			print l
	else:
		print "Case #%d:" % t
		print "Impossible"