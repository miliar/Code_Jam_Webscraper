for _ in range(input()):
	a, k = raw_input().split()
	k = int(k)

	n = 0
	for i in range(len(a) - k + 1):
		if a[i] == "-":
			a = a[:i] + "".join("-+"[c == "-"] for c in a[i:i+k]) + a[i+k:]
			n += 1
	print "Case #%d:" % (_ + 1), "-" in a and "IMPOSSIBLE" or n
