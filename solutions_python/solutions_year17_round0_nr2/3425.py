T = int(raw_input())
for x in xrange(1, T + 1):
	s = raw_input()
	S = list(s)
	i = len(S) - 1
	A = S[:]
	A.sort()
	if i == 0:
		print "Case #{}: {}".format(x,S[0])
	elif A == S:
		print "Case #{}: {}".format(x,''.join(S))
	else:
		while i >= 0:
			S[i] = "9"
			i -= 1
			while S[i] == "0":
				S[i] = "9"
				i -= 1
			S[i] = str(int(S[i]) - 1)
			L2 = S[:]
			L2.sort()
			if L2 == S:
				break
			k = 0
		if S[0] == "0":
			S = S[1:]

		print "Case #{}: {}".format(x,''.join(S))
