T = int(raw_input())
for i in range(T):
	cake, k = raw_input().split()
	k = int(k)
	cake = '+' + cake
	cake = list(cake)
	temp = cake[0]
	count = 0
	for j in range(1, len(cake) - k + 1):
		if temp != cake[j]:
			for l in range(k):
				cake[j + l] = '-' if cake[j + l] == '+' else '+'
			count = count + 1
			temp = cake[j]
	try:
		n = cake.index('-')
	except:
		n = -1
	if n == -1:
		print 'Case #' + str(i + 1) + ': ' + str(count)
	else:
		print 'Case #' + str(i + 1) + ': IMPOSSIBLE'
