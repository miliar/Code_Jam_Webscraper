def last_tidy(n):
	a = 0
	for d in range(n, 0,-1):
		l = []
		for i in str(d):
			l.append(int(i))
		if sorted(l)==l:
			a = d
			break
	return a

t = int(input())


for i in range(t):
	n = int(input())
	tidy = last_tidy(n)
	print("""Case #{}: {}""".format(i + 1, tidy))

