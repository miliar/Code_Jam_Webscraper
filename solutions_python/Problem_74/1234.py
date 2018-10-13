def sgn(n):
	if n < 0:
		return -1
	elif n > 0:
		return 1
	else:
		return 0

T = int(raw_input())
for t in range(T):
	s = raw_input()
	s = s.split(' ')
	N = int(s[0])
	b = 1
	o = 1
	cnt = 0
	nextB = [None] * (N + 1)
	nextO = [None] * (N + 1)
	nextB[N] = nextO[N] = 1000000
	for i in range(N - 1, -1, -1):
		r = s[i * 2 + 1]
		p = int(s[i * 2 + 2])
		if r == 'B':
			nextB[i] = p
			nextO[i] = nextO[i + 1]
		else:
			nextO[i] = p
			nextB[i] = nextB[i + 1]
	for i in range(N):
#		print i
		r = s[i * 2 + 1]
		p = int(s[i * 2 + 2])
		pushing = False
		while not pushing:
#			print b, o
			cnt += 1
			if (r == 'B' and p == b) or (r == 'O' and p == o):
				pushing = True
			b += sgn(nextB[i] - b)
			o += sgn(nextO[i] - o)
	print "Case #" + str(t + 1) + ': ' + str(cnt)

