import sys

def next(N):
	N = list(N)
	for b in range(len(N)-1, -1, -1):
		for a in range(len(N)-1, b, -1):
			if N[b] < N[a]:
#				print N, a, b
				s = N[a]
				N[a] = N[b]
				N[b] = s
#				print N
				R = N[:b+1]
#				print R
				ds = N[b+1:]
				ds.sort()
#				print R, ds
				R += ds
				return R
				
	digs = [n for n in N if n > '0']
	digs.sort()
#	print digs
	zeros = [n for n in N if n == '0']
#	print zeros
	R = [digs.pop(0)]
	R += zeros
	R += ['0']
	R += digs		
	return R	
T = int(sys.stdin.readline())
for case in range(T):
	print "Case #%d:" % (case+1),
	N = sys.stdin.readline().rstrip()
	print ''.join(next(N))