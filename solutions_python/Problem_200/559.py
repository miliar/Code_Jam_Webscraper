def fixNumber(l):
	done = True
	for i in xrange(1, len(l)):
		if l[i-1] > l[i]:
			done = False
			l[i-1] -= 1
			for j in xrange(i, len(l)):
				l[j] = 9
	if not done:
		fixNumber(l)
			
T = input()
for TC in xrange(1, T+1):
	N = map(int, list(raw_input()))
	fixNumber(N)
	#:N = bruteForce(N)
	print "Case #{}: {}".format(TC, int(''.join(map(str, N))))
