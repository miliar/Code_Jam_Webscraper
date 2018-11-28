def CountElement(A, B):

	Res = 0
	Map = {}

	for n in range(A, B):

		n_s = str(n)
		size = len(n_s)
		l = []
		for i in range(1, size):
			
			v = int(n_s[i:] + n_s[:i])
			if (n < v and v <= B):
				
				if l.count(v) == 0:
					l.append(v)
					Res = Res + 1
							

	return Res

f = open("input")
T = int(f.readline())
for t in range(0, T):
	values = f.readline().split()
	print "Case #%d: %d" % (t + 1, CountElement(int(values[0]), int(values[1])))
			
