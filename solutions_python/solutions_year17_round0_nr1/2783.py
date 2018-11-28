for t in xrange(1, input() + 1):
	S, k = raw_input().split()
	k, n, S = int(k), len(S), list(S)
	ans = 0
	for i in xrange(n - k + 1):
		if S[i] == '-':
			for j in xrange(i, i + k):
				S[j] = ['+', '-'][S[j] == '+']
			ans += 1
	print "Case #" + str(t) + ": " + [str(ans), "IMPOSSIBLE"]['-' in S]