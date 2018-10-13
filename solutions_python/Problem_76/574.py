inp = file("inp")
T = int(inp.readline())
for i in range(T):
	N = int(inp.readline())
	C = map(int, inp.readline().split(" "))
	sean_final = 0
	for q in xrange(1, 2**N - 1):
		pat = 0
		pat_sean = 0
		sean = 0
		j = 0
		while j < len(C):
			p = q % 2
			q /= 2
			if p == 0:
				pat = pat ^ C[j]
			else:
				pat_sean = pat_sean ^ C[j]
				sean += C[j]
			j += 1
		if pat == pat_sean:
			sean_final = max(sean_final, sean)
	if sean_final == 0:
		print "Case #" + str(i + 1) + ": NO"
	else:
		print "Case #" + str(i + 1) + ": " + str(sean_final)
