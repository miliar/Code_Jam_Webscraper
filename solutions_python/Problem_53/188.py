from sys import stdin

T = int(stdin.readline())

for case in range(T):
	(N,K) = map(int,stdin.readline().split(' '))
	K2 = K+1
	for i in range(N):
		K /= 2
		K2 /= 2
	print "Case #%d: %s" % (case+1,'ON' if K%2!=K2%2 else 'OFF')
