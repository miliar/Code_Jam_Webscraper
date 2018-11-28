
din = open('large.in','r')
dout = open('large.out','w')

T = int(din.readline())

for K in range(1,T+1):
	line = list(din.readline().split())
	print line
	row = int(line[0])
	col = int(line[1])
	grid = []
	for i in range(row):
		tmp = list(din.readline())
		tmp.remove('\n')
		for j in range(1,len(tmp)):
			if tmp[j] == '?':
				tmp[j] = tmp[j-1]
		for j in range(len(tmp)-2, -1, -1):
			if tmp[j] == '?':
				tmp[j] = tmp[j+1]
		grid.append(tmp)

	for i in range(1,len(grid)):
		if grid[i].count('?') == len(grid[i]):
			grid[i] = grid[i-1]

	for i in range(len(grid)-2,-1,-1):
		if grid[i].count('?') == len(grid[i]):
			grid[i] = grid[i+1]

	dout.write('Case #%d:\n' % K)
	for item in grid:
		dout.write('%s\n' % ''.join(item))

	
din.close()
dout.close()