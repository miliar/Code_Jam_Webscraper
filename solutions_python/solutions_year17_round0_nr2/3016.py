t = input()
tc = 1
while t:
	t -= 1
	n = input()
	a = map(int, list(str(n)))
	n = len(a)
	done = 1
	i = 0
	while i+1 < n and done:
		if a[i] > a[i+1]:
			a[i] -= 1
			done = 0
			mark = i
			while i - 1 >= 0:
				if a[i-1] > a[i]:
					a[i-1] -= 1
					mark = i - 1
				else:
					break
				i -= 1
		i += 1
	if not done:
		for i in range(mark+1, n):
			a[i] = 9
	n = int(''.join(map(str, a)))
	print "Case #{0}: {1}".format(tc, n)
	tc += 1
