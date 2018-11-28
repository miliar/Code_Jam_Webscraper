def solve(pancakes, k):
	#pancakes = "0"*(k-1) + pancakes
	n = [int(s) for s in pancakes.replace("+", "1").replace("-", "0")]

	sols = [0] * (len(pancakes) - k + 1)

	for i in range(len(pancakes) - k + 1):
		sols[i] += n[i] + 1

		for j in range(1, k):
			index = i - j
			value = 0
			if i - j >= 0:
				value = sols[i - j]

			sols[i] += value
		sols[i] %= 2

	test = n
	for index, v in enumerate(sols):
		x = [0]*len(n)
		for i in range(k):
			x[i + index] = 1

		y = [v*a for a in x]
		test = [(a + b) % 2 for a,b in zip(test, y)]

	if 0 in test:
		return "IMPOSSIBLE"
	else:
		return sum(sols)



t = int(raw_input())

for i in xrange(1, t + 1):
	inp = raw_input().split(" ")
	pancakes = inp[0]
	k = int(inp[1])

 	print "Case #{}: {}".format(i, solve(pancakes, k))
 