def solve(st):
	r = 0
	k = 0
	for ind,c in enumerate(st):
		if k < ind:
			r += ind-k
			k = ind
		k += int(c)
	return r


n = input()
for i in range(int(n)):
	q, s = input().split(' ')
	r = solve(s)
	print('Case #%s: %s' % (i+1,r))

