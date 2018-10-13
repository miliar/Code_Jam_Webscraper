from pprint import pprint

ni = int(raw_input())

for i in range(ni):
	e, c = raw_input().split(' ')
	e = int(e)
	c = int(c)

	rootDir = {}
	for j in range(e):
		inpath = raw_input().split("/")[1:]
		curDir = rootDir
		for sp in inpath:
			if curDir.has_key(sp):
				curDir = curDir[sp]
			else:
				curDir[sp] = {}
				curDir = curDir[sp]

	created = 0
	for j in range(c):
		inpath = raw_input().split("/")[1:]
		curDir = rootDir
		for sp in inpath:
			if curDir.has_key(sp):
				curDir = curDir[sp]
			else:
				curDir[sp] = {}
				curDir = curDir[sp]
				created = created+1

	print "Case #%d: %d"%(i+1, created)


