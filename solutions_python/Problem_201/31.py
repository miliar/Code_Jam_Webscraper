from sys import stdin
readline = stdin.readline

def ans(N, K):
	if K == 1:
		if N%2 == 0:
			return N/2, N/2-1
		if N%2 == 1:
			return (N-1)/2, (N-1)/2
	
	if N%2 == 0:
		splits = (N/2, N/2-1)
	else:
		splits = ((N-1)/2, (N-1)/2)
	
	if K%2 == 0:
		return ans(max(splits), K/2)
	else:
		return ans(min(splits), (K-1)/2)

T = int(readline())

for t in xrange(1, T+1):
	N, K = map(int, readline().strip().split())
	y, z = ans(N, K)
	
	print "Case #%d: %d %d" % (t, y, z)
