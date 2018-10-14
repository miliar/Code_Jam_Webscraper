import sys

def check(N, K, rows_, i, j):
	c = rows_[i][j]
	
	if j+K <= N:
		found = True
		for k in range(K):
			if rows_[i][j+k] != c:
				found = False
				break
		if found:
			return c

	if i+K <= N:
		found = True
		for k in range(K):
			if rows_[i+k][j] != c:
				found = False
				break
		if found:
			return c

	if i+K <= N and j+K <= N:
		found = True
		for k in range(K):
			if rows_[i+k][j+k] != c:
				found = False
				break
		if found:
			#print "Found1 at (%d,%d)" % (i,j)
			return c

	if i+K <= N and j-K+1 >= 0:
		found = True
		for k in range(K):
			if rows_[i+k][j-k] != c:
				found = False
				break
		if found:
			#print "Found2 at (%d,%d)" % (i,j)
			return c
		
	return ''

def f(N, K, rows):
	for row in rows:
		vacant = -1
		for i in range(N):
			if row[N-i-1] != '.' and vacant >= 0:
				row[vacant] = row[N-i-1]
				row[N-i-1] = '.'
				vacant -= 1
			if row[N-i-1] == '.':
				vacant = max(vacant,N-i-1)

	Red,Blue = False,False
	for i in range(N):
		for j in range(N):
			if rows[i][j] != '.':
				chk = check(N, K, rows, i, j)
				if chk == 'R':
					Red = True
				elif chk == 'B':
					Blue = True
	if Red and Blue:
		return "Both"
	elif Red:
		return "Red"
	elif Blue:
		return "Blue"
	else:
		return "Neither"

inf = open(sys.argv[1])
T = int(inf.readline())
for i in range(T):
	N, K = [int(x) for x in inf.readline().split()]
	rows = []
	for j in range(N):
		row = list(inf.readline().strip())
		rows.append(row)
	result = f(N, K, rows)
	print "Case #%d: %s" % (i+1, result)
