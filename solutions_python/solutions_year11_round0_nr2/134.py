import sys

a = int(sys.stdin.readline())

for i in xrange(a):
	line = sys.stdin.readline().split()

	ok = {}
	nok = {}

	c = int(line[0])
	for x in line[1:c+1]:
		ok[x[0]+x[1]] = x[2]
		ok[x[1]+x[0]] = x[2]
	
	for x in line[c+2:-2]:
		if x[0] in nok:
			nok[x[0]].append(x[1])
		else:
			nok[x[0]] = [x[1]]
		if x[1] in nok:
			nok[x[1]].append(x[0])
		else:
			nok[x[1]] = [x[0]]
	
	res = []
	
	ellist = line[-1]
	for x in ellist:
		if len(res) > 0 and res[-1]+x in ok:
			res[-1] = ok[res[-1]+x]
		else:
			for r in nok.get(x,[]):
				if r in res:
					res = []
					break
			else:
				res.append(x)
	
	print "Case #%d: [%s]" % (i+1, ", ".join(res))
