for _ in range(input()):
	a = map(int, raw_input())
	b = a * 1


	i = len(a) - 1

	while i:
		if a[i] < a[i - 1]:
			for j in range(i, len(a)): a[j] = 9
			i -= 1
			a[i] -= 1
		else: i -= 1

	assert a <= b

	print "Case #%d:" % (_ + 1), "".join(map(str, a)).lstrip("0")
