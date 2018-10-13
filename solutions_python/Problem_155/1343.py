fin = open("A-large.in","r")
fout = open("data.out","w")

T = int(fin.readline())

for t in range(T):
	inp = fin.readline().split()

	maxS = int(inp[0])

	stding = 0
	frds = 0

	for k in range(len(inp[1])):
		p = int(inp[1][k])
	
		if k == 0:
			stding += p
		else:
			if stding < k:
				need = k-stding
				frds += need
				stding += need
			stding += p

	fout.write("Case #%d: %d\n" % (t+1,frds))
