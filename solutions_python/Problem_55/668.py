for C in xrange(1, input()+1):
	R, K, N = map(int, raw_input().split())
	list = map(int, raw_input().split())
	dict = {}
	i = 0
	res = 0
	while R > 0:
		if i in dict:
			res += dict[i][1]
		else:
			count = 0
			for j in xrange(N):
				count += list[(i+j)%N]
				if count + list[(i+j+1)%N] > K:
					dict[i] = [j+1, count]
					break
			if i not in dict:
				dict[i] = [N, count]
			res += count
		R -= 1
		i = (i+dict[i][0])%N
	print "Case #%d: %d" % (C, res)
