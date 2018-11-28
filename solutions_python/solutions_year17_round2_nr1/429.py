import sys

sys.stdin = open('A-large.in')
sys.stdout = open('A-large.out', 'w')

def solve():
	D, N = map(int, sys.stdin.readline().strip().split())
	
	times = []
	for i in xrange(N):
		K, S = map(int, sys.stdin.readline().strip().split())
		if (K < D):
			times.append(1.0*(D-K)/S)
	return D / max(times)

T = int(sys.stdin.readline())
for x in xrange(T):
	print("Case #" + str(x+1) + ": " + "%.6f" % solve())