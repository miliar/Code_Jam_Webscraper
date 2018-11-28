import sys

P = [ int(s) for s in open('cl.txt').readlines() ]

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	ar = sys.stdin.readline().split()
	A = int(ar[0])
	B = int(ar[1])
	ans = 0
	for p in P:
		if A <= p <= B:
			ans += 1
	print "Case #%d: %d" % (T, ans)
