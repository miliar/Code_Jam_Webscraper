import sys

T=int(sys.stdin.readline())

for case in range(T):
	print "Case #%d:" % (case+1)
	R,C = map(int, sys.stdin.readline().split(' '))
	M = []
	for r in range(R):
		M.append(list(sys.stdin.readline().strip()))
#	print M
	for r in range(R-1):
		for c in range(C-1):
			if M[r][c] == '#' and M[r+1][c] == '#' and M[r][c+1] == '#' and M[r+1][c+1] == '#':
				M[r][c] = '/'
				M[r][c+1] = '\\'
				M[r+1][c] = '\\'
				M[r+1][c+1] = '/'
	
	possible = True
	for r in range(R):
		for c in range(C):
			if M[r][c] == '#':
				possible = False
				break
	
	if possible:
		for r in range(R):
			print "".join(M[r])
	else:
		print 'Impossible'
				
	
	
