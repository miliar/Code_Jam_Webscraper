input = open('C-small-attempt0.in', 'r')
output = open('C-small.out', 'w')
t = int(input.readline())
for caseId in range(t):
	(R, k, n) = map(int, input.readline().split(' '))
	g = map(int, input.readline().split(' '))
	i = 0
	a = 0L
	for r in range(R):
		j = i
		c = 0
		while c + g[i] <= k:
			c += g[i]
			i += 1
			if i == n:
				i = 0
			if i == j:
				break
		a += c

	print >>output,"Case #%d: %d" % (caseId + 1, a)

output.close()
