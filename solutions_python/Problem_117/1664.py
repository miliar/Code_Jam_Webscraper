import sys

def verify_mown(A, N, M):
	mn = map(max, A)
	mm = []
	for m in range(M):
		maxv = 0
		for n in range(N):
			maxv = max(maxv, A[n][m])
		mm.append(maxv)
	for n in range(N):
		for m in range(M):
			if A[n][m] < mn[n] and A[n][m] < mm[m]:
				return False
	return True

T = int(sys.stdin.readline())
for t in range(T):
    N, M = map(int, sys.stdin.readline().split(' '))
    A = []
    for n in range(N):
        A.append(map(int, sys.stdin.readline().split(' ')))
    print "Case #%d: %s" % (t + 1, "YES" if verify_mown(A, N, M) else "NO")