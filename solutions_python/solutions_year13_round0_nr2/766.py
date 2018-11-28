Y = "YES"
N = "NO"
T = int(raw_input())
for cas in xrange(1, T + 1):
	print "Case #" + str(cas) + ":",
	n, m = map(int, raw_input().split())
	matrix = list()
	rmax = list()
	cmax = list()
	for r in xrange(0, n):
		row = map(int, raw_input().split())
		rmax.append(max(row))
		matrix.append(row)
	for c in xrange(0, m):
		cmax.append(max(map(lambda item: item[c], matrix)))
	flag = True
	for i in xrange(0, n):
		for j in xrange(0, m):
			if matrix[i][j] < rmax[i] and matrix[i][j] < cmax[j]:
				flag = False
				break
			if not flag: break
	print Y if flag else N
