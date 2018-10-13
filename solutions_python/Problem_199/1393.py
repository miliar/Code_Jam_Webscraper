# Woooo! Trying the (not-that-) new hammer (python, that is) on ALL THE NAILZ!

# basically input() gets the line sans newline
tc = int(input())  # of test cases
for cc in range(1, tc + 1):
	s, n = [x for x in input().split(" ")]
	flips = 0
	k = int(n)
	s = list(s)

	while len(s) >= k:
		# i = s.find('-')  # downside to using lists...

		if '-' in s:
			i = s.index('-')
		else:
			i = -1

		if i == -1:
			break

		del s[:i]

		# ran out of flip space, still found unhappy
		if len(s) < k:
			flips = -1
			break

		# awkwardest flipper ever?
		flips += 1
		for f in range(k):
			if s[f] == '+': s[f] = 't'
			if s[f] == '-': s[f] = '+'
			if s[f] == 't': s[f] = '-'


	if flips == -1:
		res = 'IMPOSSIBLE'
	else:
		res = flips
	print("Case #{}: {}".format(cc, res))