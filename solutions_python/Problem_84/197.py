red = ['/', '\\', '\\', '/']
def turn_red(X, Y, P):
	count = 0
	for x in range(X, X + 2):
		for y in range(Y, Y + 2):
			if P[x][y] != '#':
				return False
	for x in range(X, X + 2):
		for y in range(Y, Y + 2):
			P[x][y] = red[count]
			count += 1
	return True
f = open('in', 'r')

T = int(f.readline()[:-1])
for case_no in range(1, T + 1):
	R, C = map(int, f.readline()[:-1].split(' '))
	P = list()
	for i in range(R):
		P.append(list(f.readline()[:-1]))
	#for p in P:
		#print ''.join(p)
	for x in range(R - 1):
		for y in range(C - 1):
			turn_red(x, y, P)
	if '#' not in ''.join(''.join(p) for p in P):
		print "Case #%s:" % (case_no)
		for p in P:
			print ''.join(p)
	else:
		print "Case #%s:" % (case_no)
		print 'Impossible'
