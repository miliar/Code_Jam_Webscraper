import sys

T=int(sys.stdin.readline())

INF=100000000000000

for case in range(T):
	print "Case #%d:" % (case+1),
	N,L,H = map(int, sys.stdin.readline().split(' '))
	NTS = map(int, sys.stdin.readline().split(' '))
	ok = False
	for n in range(L, H+1):
		ok = True
		for other in range(N):
			if n % NTS[other] != 0 and NTS[other] % n != 0:
				ok = False
				break
		if ok:
			print n
			break
	if not ok:
		print 'NO'
