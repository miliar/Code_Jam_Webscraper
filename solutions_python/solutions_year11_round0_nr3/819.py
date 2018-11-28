def solver(S):
	L = map(int, S.split())
	if not reduce(lambda x, y: x^y, L):
		L.sort()
		return str(reduce(lambda x,y: x+y, L[1:]))
	return 'NO'

		
f = open("test.out", 'w')
cases = open("test.in", 'r').readlines()[1:][1::2]
for i in range(0, len(cases)):
	line = "Case #" + str(i+1) + ": " + solver(cases[i])
	print line
	f.write(line + "\n")
f.close()