T = int(raw_input())
for t in xrange(T):
	[N, P] = [int(x) for x in raw_input().split(' ')]
	# min who doesnt win
	mi = 0
	if P == 2**N:
		mi = 2**N - 1
	elif P & (2**(N-1)) == 0:
		mi = 0
	else:
		mi = 0
		n = 1
		while n <= N and (P & (2**(N-n))) != 0:
			mi += 2**(n-1)
			n+=1
		if P % (2**(N-n)) != 0: mi += 2**(n-1)
		mi -= 1
	# max who wins

	ma = 2**N-1
	if P != 2**N:
		ma -= 1
		n = 1
		while n <= N and (P & (2**(N-n))) == 0:
			ma -= 2**n
			n += 1
			
	print "Case #%d: %d %d" % (t+1, mi, ma)


