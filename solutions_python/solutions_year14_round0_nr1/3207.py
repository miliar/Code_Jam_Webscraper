with open("a.in", 'r') as f:
	T = int(f.readline())
	for t in range(1, T+1):
		S = set(range(1, 17))
		for i in range(2):
			n = int(f.readline())
			for j in range(1, 5):
				line = f.readline()
				if n == j:
					S = S & set(map(int, line.split()))
		if len(S) == 0:
			print("Case #%d: Volunteer cheated!" % t)
		elif len(S) > 1:
			print("Case #%d: Bad magician!" % t)
		else:
			print("Case #%d: %d" % (t, list(S)[0]))
