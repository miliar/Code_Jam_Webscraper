def calc(grid, pos, lr):
	if lr:
		k = 0
		for q in xrange(pos-1,-1,-1):
			if grid[q] == '.':
				k+=1
			elif grid[q] == 'X':
				return k
	else:
		k = 0
		for q in xrange(pos+1,len(grid)):
			if grid[q] == '.':
				k+=1
			elif grid[q] == 'X':
				return k

nc = input()

for i in xrange(1,nc+1):
	n,k = map(int, raw_input().split(" "))

	grid = list('X' + '.'*n + 'X')

	for q in xrange(0,k):
		mins = []	
		for j in xrange(0,len(grid)):
			if grid[j] == '.':
				le = calc(grid, j, True)
				re = calc(grid, j, False)
				mins.append((j, min(le,re), max(le,re)))

		val = max(mins, key = lambda x: x[1])
		p = val[0]
		dist= val[1]
		count = 0
		maxs = []
		for z in mins:
			if z[1] == dist:
				maxs.append(z)
				count += 1

		if count == 1:
			grid[p] = 'X'
		else:
			p = max(maxs, key=lambda x:x[2])[0]
			grid[p] = 'X'
		if q == k-1:
			le = calc(grid, p, True)
			re = calc(grid, p, False)
			print "Case #%d: %d %d"%(i,max(le,re), min(le,re))

