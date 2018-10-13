from sys import stdin

def solve(N, M, lawn):
	for n in xrange(N):
		for m in xrange(M):
			h = lawn[n][m]
			hor = True
			for i in xrange(M):
				if lawn[n][i] > h:
					hor = False
					break
			ver = True
			for j in xrange(N):
				if lawn[j][m] > h:
					ver = False
					break
			if (not hor) and (not ver):
				return 'NO'
	return 'YES'

T = int(stdin.readline())
for t in xrange(T):
	N, M = map(int, stdin.readline().split())
	lawn = []
	for n in xrange(N):
		row = map(int, stdin.readline().split())
		lawn.append(row)
	answer = solve(N, M, lawn)
	print 'Case #%d:' % (t + 1), answer