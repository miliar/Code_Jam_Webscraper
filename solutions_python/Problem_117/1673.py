import sys

f = open('b.in', 'r')

x = int(f.readline())

for i in range(x):
	m, n = [int(j) for j in f.readline().split(' ')]
	rows = []
	cols = []
	res = []
	tmp = []
	for j in range(n): tmp.append(False)
	for j in range(m): res.append(list(tmp))
	for j in range(n): cols.append([])
	for j in range(m):
		inp = [int(k) for k in f.readline().split(' ')]
		rows.append(inp)
		for k in range(len(inp)):
			cols[k].append(inp[k])

	for j in range(m):
		mm = max(rows[j])
		for k in range(n):
			if rows[j][k] == mm:
				res[j][k] = True
	
	for j in range(n):
		mm = max(cols[j])
		for k in range(m):
			if cols[j][k] == mm:
				res[k][j] = True

	soln = all([all(j) for j in res])
	print "Case #%d: %s" %(i+1, "YES" if soln else "NO")
