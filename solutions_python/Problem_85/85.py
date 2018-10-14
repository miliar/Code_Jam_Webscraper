import sys

T=int(sys.stdin.readline())

INF=100000000000000

def solve(A, B, t, C):
#	print A,B,t,C
	d = []
	for k in range(C+1):
		l = [INF]*(B+1)
		d.append(l)
	
	d[0][B] = 0

	for k in range(1,C+1):
		for b in range(B, -1, -1):
			v = d[k][b]
			v = min(v, d[k-1][b] + A[k-1]*2)
			if b == B-1 and t > 0:
				if t < A[k-1]*2:
					v = min(v, d[k-1][b+1] + A[k-1] + t/2)
			elif b < B:
				v = min(v, d[k-1][b+1] + A[k-1])
			d[k][b] = v
		t -= A[k-1]*2
	mv = INF
	mb = -1		
#	print d
	for b in range(B+1):
		if d[C][b] < mv:
			mv = d[C][b]
			mb = b
	return (mv, mb)		
	

for case in range(T):
	print "Case #%d:" % (case+1),
	line = map(int, sys.stdin.readline().split(' '))
	L, t, N, C = line[:4]
	A = line[4:]
	segs = (N-1)/C + 1
	s = solve(A*((N/C)+1), L, t, N)
#	print s
	print s[0]
	
