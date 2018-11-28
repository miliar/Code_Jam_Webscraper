import sys

T = int(sys.stdin.readline())
MAX = 10000000

def ro(S, x):
	while True:
		pa = S.get(x, x)
		if pa == x:
			S[pa] = x
			return x
		x = pa

def jo(S, a, b):
	ra = ro(S, a)
	rb = ro(S, b)
	if(ra < rb):
		S[rb] = ra
	else:
		S[ra] = rb
	

for i in range(T):
	(H, W) = map(int, sys.stdin.readline().split(' '))
	M = []
	R = []
	for r in range(H):
		M.append(map(int, sys.stdin.readline().split(' ')))
		R.append([' ']*W)
	print "Case #%d: " % (i+1)
#	print M
	P = {}
	for x in range(H):
		for y in range(W):
			NA = MAX
			WA = MAX
			EA = MAX
			SA = MAX
			if y>0:
				WA = M[x][y-1]
			if x>0:
				NA = M[x-1][y]
			if y<W-1:
				EA = M[x][y+1]
			if x<H-1:
				SA = M[x+1][y]
			mm = min([NA, WA, EA, SA]);
			if(mm >= M[x][y]):
				ro(P, (x,y))
				continue;
			if(NA == mm):
				jo(P, (x-1,y), (x,y))
			elif(WA == mm):
				jo(P, (x,y-1), (x,y))
			elif(EA == mm):
				jo(P, (x,y+1), (x,y))
			elif(SA == mm):
				jo(P, (x+1,y), (x,y))

	X = 'a'
	for x in range(H):
		for y in range(W):
			if P[(x,y)] == (x,y):
				R[x][y] = X
				X = chr(ord(X) + 1)
#			print P[(x,y)],
#		print ";"
	for x in range(H):
		for y in range(W):
			root = P[(x,y)]
			R[x][y] = R[root[0]][root[1]]

	for x in range(H):
		print ' '.join(R[x]);