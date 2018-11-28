
T = int(raw_input())

for t in range(1, T+1):
	R, C = tuple(map(int, raw_input().split()))
	m = []
	for i in range(R):
		m.append(list(raw_input()))
	to_cover = []
	
	for i in range(R):
		for j in range(C):
			if m[i][j] == '#':
				to_cover.append((i, j))
	
	to_cover.sort()
	possible = True
	while to_cover and possible:
		i, j = to_cover[0]
		to_cover = to_cover[1:]
		
		if m[i][j] != '.' and m[i][j] != '#':
			continue
		
		# outside?
		if i >= R-1 or j >= C-1:
			possible = False
			break
		# not blue?
		for a in range(2):
			for b in range(2):
				if m[i+a][j+b] != '#':
					possible = False
					break
		m[i][j] = '/'
		m[i+1][j] = '\\'
		m[i][j+1] = '\\'
		m[i+1][j+1] = '/'
		
	
	print 'Case #%d:' % t
	if possible:
		for r in m:
			print ''.join(r)
	else:
		print 'Impossible'
