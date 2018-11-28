def solve(s, k):
	s = [1 if i == '+' else -1 for i in s]
	count = 0

	while -1 in s:
		loc = s.index(-1)
		if loc > len(s)-k:
			return 'IMPOSSIBLE'
		for x in range(loc, loc+k):
			s[x] *= -1
		count += 1

	return str(count)

if __name__ == '__main__':
	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
	  s, k = [o for o in raw_input().split(" ")]
	  k = int(k)
	  print "Case #{}: {}".format(i, solve(s,k))