
T = int(raw_input())
for TC in xrange(1, T+1):
	R, C = map(int, raw_input().split())
	Z = []
	for i in xrange(R):
		Z.append([x for x in raw_input()])

	for i in range(R):	
		for j in range(1, C):
			if Z[i][j] == '?':
				Z[i][j] = Z[i][j-1]
		for j in range(C-1, 0, -1):
			if Z[i][j-1] == '?':
				Z[i][j-1] = Z[i][j]

	for i in range(1, R):
		if Z[i][0] == '?':
			Z[i][:] = Z[i-1][:]
	for i in range(R-1, 0, -1):
		if Z[i-1][0] == '?':
			Z[i-1][:] = Z[i][:]

	print "Case #%d:"%(TC)
	for z in Z:
		print "".join(z)	


