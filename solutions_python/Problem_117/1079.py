
T = int(raw_input())
for i in range(T):
	a = []
	temp = raw_input().split(' ')
	N = int(temp[0])
	M = int(temp[1])
	print "Case #" + str(i+1) + ":",	
	for j in range(N):
		a.append([int(x) for x in raw_input().split(' ')])
	possible = True
	for n in range(0,N):
		for m in range(0,M):
			row_max = a[n][m]
			column_max = a[n][m]
			for k in range(N):
				if a[k][m] > row_max:
					row_max = a[k][m]
			for k in range(M):
				if a[n][k] > column_max:
					column_max = a[n][k]
			if row_max > a[n][m] and column_max > a[n][m]:
				print "NO"
				possible = False
				break
		if not possible:
			break
	if possible:
		print "YES" 	
	
