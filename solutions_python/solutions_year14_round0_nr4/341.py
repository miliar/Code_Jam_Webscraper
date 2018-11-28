import sys

TT = int(sys.stdin.readline())

def wincnt(A, B):
	ans, bb = 0, 0
	for a in A:
		if a > B[bb]: ans += 1
		else: bb += 1
	return ans

for T in xrange(1,TT+1):
	N = int(sys.stdin.readline())
	A = sorted(map(float, sys.stdin.readline().split()), reverse=True)
	B = sorted(map(float, sys.stdin.readline().split()), reverse=True)

	ans1 = N-wincnt(B, A)
	ans2 = wincnt(A, B)

	print "Case #%d: %d %d" % (T, ans1, ans2)

