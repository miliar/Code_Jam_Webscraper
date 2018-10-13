f = open('1.in','r')
o = open('out.dat','w')

n = int(f.readline())

def alive(A,xmax,ymax):
	for i in xrange(1,xmax+1):
		for j in xrange(1,ymax+1):
			if A[i][j]:
				return 1;
	return 0

for i in xrange(n):
	o.write('Case #' + str(i+1) + ': ')
	
	R = int(f.readline())
	P = [[None]*4 for x in xrange(R)]
	for x in xrange(R):
		P[x] = [int(j) for j in f.readline().split()]
	
	xmax = 0;
	ymax = 0;
	
	for x in xrange(R):
		if ymax < P[x][3]:
			ymax =P[x][3]
		if xmax < P[x][2]:
			xmax =P[x][2]
			
	A = [[0]*(ymax+1) for x in xrange(xmax+1)]
	
	for a in xrange(R):
		for b in xrange(P[a][0],P[a][2]+1):
			
			for c in xrange(P[a][1],P[a][3]+1):
				A[b][c] = 1;
	
	t = 0

	
	while alive(A,xmax,ymax):
		t+=1
		for i in xrange(xmax,0,-1):
			for j in xrange(ymax,0,-1):
				if A[i][j]:
					if not(A[i-1][j] or A[i][j-1]):

						A[i][j] = 0
				else:
					if (A[i-1][j] and A[i][j-1]):
						A[i][j] = 1


	
	
	o.write(str(t)+ '\n')
