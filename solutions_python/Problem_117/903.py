import sys

f = sys.stdin
lines = f.read().split('\n');

nbCases = int(lines[0])
countl = 1

for i in range(0, nbCases):
	l = lines[countl].split(' ')
	countl += 1
	n = int(l[0])
	m = int(l[1])
	
	lawnlines = [100 for j in range(0, n)]
	lawncolumns = [100 for k in range(0, m)]
	
	s = [[ 100 for j in range(0, m)] for k in range(0, n)]
	
	for j in range(0, n):
		l = lines[countl].split(' ')
		countl += 1
		for k in range(0, m):
			s[j][k] = int(l[k])
	
	
	for x in range(100, 0, -1):
		#check lines
		for j in range(0, n):
			if max(s[j]) <= x:
				lawnlines[j] = x
		
		#check columns
		for k in range(0, m):
			t = []
			for j in range(0, n):
				t.append(s[j][k])
			if max(t) <= x:
				lawncolumns[k] = x
	
	good = "YES"
	for j in range(0, n):
		for k in range(0, m):
			if s[j][k] != min(lawnlines[j], lawncolumns[k]):
				good = "NO"

	print "Case #%s: %s" % (i+1, good)
				