T = int(raw_input())
for t in range(T):
	N,K = map(lambda x: int(x), raw_input().strip('\n').split(' '))
	u = len(bin(K)) - 2; x = N >> u
	print "Case #{0}: {1} {2}".format(t+1, x, x if (N >> (u-1)) % 2 == 1 else max(x-1,0))
