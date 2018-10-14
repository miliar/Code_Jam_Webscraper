for i in range(int(input())):
	nstr = input()
	ns = [int(ch) for ch in nstr]
	j = 0
	while j < len(ns) - 1 and ns[j] <= ns[j + 1]:
		j += 1
	if j == len(ns) - 1:
		print("Case #%d: %s" % (i + 1, nstr))
	else:
		while j > 0 and ns[j - 1] == ns[j]:
			j -= 1
		if j == 0:
			if ns[0] == 1:
				print("Case #%d: %s" % (i + 1, "9" * (len(ns) - 1)))
			else:
				print("Case #%d: %d%s" % (i + 1, ns[0] - 1, "9" * (len(ns) - 1)))
		else:
			print("Case #%d: %s%d%s" % (i + 1, nstr[:j], ns[j] - 1, "9" * (len(ns) - j - 1)))