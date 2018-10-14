def find_recycled(n, b):
	ns = str(n)
	reclist = []
	for i in xrange(1, len(ns), 1):
		nrec = ns[i:len(ns)] + ns[0:i]
		if nrec[0] != "0":
			nrec = eval(nrec)
			if nrec <= b and nrec > n and (n, nrec) not in reclist:
				reclist.append((n,nrec))
	return reclist

inp = file("input.in")
T = eval(inp.readline())
out = file("output.txt", "w")

d = []
for n in xrange(12, 2000000, 1):
	d.extend(find_recycled(n, 2000000))

for i in xrange(T):
	a, b = inp.readline().strip().split()
	a = eval(a)
	b = eval(b)
	nrec = 0
	for item in d:
		if item[0] > b:
			break
		if item[0] >= a and item[1] <= b:
			nrec += 1
	out.write("Case #%d: %d\n" %(i + 1, nrec))
			
