cases = int(raw_input())
for c in range(1, cases+1):
	cakes, w = raw_input().split()
	cakes = [cake for cake in cakes]
	w = int(w)
	res = 0
	for i in range(0, len(cakes)-w+1):
		if cakes[i] == '-':
			res += 1
			for j in range(w):
				cakes[i+j] = '-' if cakes[i+j] == '+' else '+'
	if '-' in cakes:
		res = -1
	print "Case #" + str(c) + ": " + ("IMPOSSIBLE" if res == -1 else str(res))
