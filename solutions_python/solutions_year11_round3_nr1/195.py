from sys import stdin

t = int(stdin.readline())

for tc in xrange(t):
	
	z = stdin.readline().split()
	n = int(z[0])
	m = int(z[1])
	
	mat = []
	for i in xrange(n):
		mat.append(stdin.readline().strip())
	
	x = [0]*m;
	table = [];
	for i in xrange(n):
		table.append([]);
		for j in xrange(m):
			table[i].append(".")
	
	ok = True
	for i in xrange(n):
		c = 0
		for j in xrange(m):
			if mat[i][j] == "#":
				if c == 0:
					if x[j] == 0:
						table[i][j] = "/"
					else:
						table[i][j] = "\\"
					x[j] = 1 - x[j]
					c = 1
				else:
					if x[j] == 0:
						table[i][j] = "\\"
					else:
						table[i][j] = "/"
					x[j] = 1 - x[j]
					c = 0
				
			elif c == 1 or x[j] == 1:
				ok = False
		if c == 1:
			ok = False
	
	for j in xrange(m):
		if x[j] == 1:
			ok = False

	print "Case #%d:" %  (tc+1)
	if ok:
		for i in xrange(n):
			print "".join(table[i])
	else:
		print "Impossible"
