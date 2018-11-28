def go(cake, r, c, R, C, rc, cc):
	if c < 0 or c >= C or r < 0 or r >= R:
		return '?'
	if cake[r][c] != '?':
		return cake[r][c]
	cake[r][c] = go(cake, r+rc, c+cc, R, C, rc, cc)
	return cake[r][c]

T = int(input())
for t in range(T):
	[R, C] = [int(x) for x in input().split(' ')]
	cake = []

	for r in range(R):
	    cake.append(list(input()))

	for r in range(R):
		for c in range(C):
			cake[r][c] = go(cake, r, c, R, C, 0, -1)
			cake[r][c] = go(cake, r, c, R, C, 0, 1)
	
	for r in range(R):
		for c in range(C):
			cake[r][c] = go(cake, r, c, R, C, -1, 0)
			cake[r][c] = go(cake, r, c, R, C, 1, 0)
			
	for r in range(R):
		for c in range(C):
			cake[r][c] = go(cake, r, c, R, C, 0, -1)
			cake[r][c] = go(cake, r, c, R, C, 0, 1)
			    
	
	print("Case #{}:".format(t+1))
	for c in cake:
		print("{}".format(''.join(c)))

	
	
