T=int(input())
for t in range(T):
	L=map(int, raw_input().split())
	R=L[0]
	C=L[1]
	cake=[]
	for r in xrange(0,R):
		cake.append(list(raw_input()))
		for c in xrange(1,C):
			if cake[r][c]=='?':
				cake[r][c]=cake[r][c-1]
			cake[r].reverse()
			if cake[r][c]=='?':
				cake[r][c]=cake[r][c-1]
			cake[r].reverse()
		if cake[r][0]=='?':
			if r>0:
				cake[r]=cake[r-1]
	cake.reverse()
	for r in xrange(1,R):
		if cake[r][0]=='?':
			cake[r]=cake[r-1]
	cake.reverse()
	print("Case #%d:"%(t+1))
	for r in xrange(0,R):
		print(''.join(cake[r]))
