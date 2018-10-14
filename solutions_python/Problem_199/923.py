
def solve(astr, k):
	cakes = [-1 if c == '-' else +1 for c in astr]
	count = 0
	js = range(1,k)
	l = len(cakes)-k+1
	for i in xrange(l):
		if cakes[i] == +1:
			continue
		count += 1
		if i+1 < l and cakes[i+1] == +1:
			count += 1
			cakes[i+k] *= -1
			continue
		for j in js:
			cakes[i+j] *= -1
	# print cakes, k
	for i in xrange(l, len(cakes)):
		if cakes[i] == -1:
			return 'IMPOSSIBLE'
	return count



for t in range(int(raw_input())):
	s, k = raw_input().strip().split()
	k = int(k)
	print "Case #{}: {}".format(t+1, solve(s, k))
