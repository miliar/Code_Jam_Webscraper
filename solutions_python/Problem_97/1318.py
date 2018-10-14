import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
	r = sys.stdin.readline().split()
	A, B = int(r[0]), int(r[1])
	res = set()
	for n in range(A, B+1):
		s = str(n)
		ll = len(s)
		for j in range(1, ll):
			ss = s[-j:] + s[0:ll-j]
			m = int(ss)
			if n < m and m <= B and (n,m) not in res:
				res.add((n,m))

	print "Case #%d: %d" % (i, len(res))
