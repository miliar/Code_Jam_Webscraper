
N = int(input())
for n in range(1,N+1):
	
	R = int(input())
	rows = [[int(c) for c in input()] for s in range(R)]
	rows = [max(i for i,n in enumerate(r) if n or not i) for r in rows]
	
	swaps = 0
	for i in range(R-1):
		if rows[i] > i:
			for j in range(i,R):
				if rows[j] <= i:
					rows.insert(i, rows.pop(j))
					swaps += j-i
					break
	
	print('Case #%s: %s' % (n, swaps))
