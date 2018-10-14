def solve():
	s,K = raw_input().split()
	K = int(K)
	s = [False if c == '-' else True for c in s]
	le = len(s)
	moves = 0

	for idx in xrange(le):
		if s[idx] == False:
			if idx+K-1 >= le:
				return 'IMPOSSIBLE'
			for j in xrange(idx,idx+K):
				s[j]^=1
			moves+=1

	return moves


if __name__ == '__main__':
	t = input()
	c = 1
	while c<=t:
		print 'Case #{}: {}'.format(c,solve())
		c+=1
