def GCD(u, v):
	while v:
		u, v = v, u % v
	return u

C = int(raw_input())

for q in range(C):
	R = raw_input().split()
	T = map(int, R[1:])
	T.sort()

	D = 0
	for i in range(1, len(T)):
		D = GCD(D, T[i] - T[i - 1])
	
	print 'Case #%d: %d' % (q + 1, (-T[0]) % D)
