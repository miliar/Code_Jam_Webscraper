def isEmpty(n):
	empty = True
	for x in n:
		empty = empty and (x=='?')

	return empty

for _ in range(int(input())):
	r,c = map(int,input().split())
	cake = []
	for i in range(r):
		s = list(input())
		cake.append(s)

	i=0
	lastRow = []
	while i < r:
		j=0
		perf = []
		while i < r and isEmpty(cake[i]):
			perf.append(i)
			i+=1
		if i == r:
			break
		last = None
		process = []
		while j < c:
			if cake[i][j] == '?':
				process.append(j)
				j+=1
			else:
				last = cake[i][j]
				for m in process:
					cake[i][m] = cake[i][j]
				process = []
				j+=1

		if j == c and cake[i][j-1] == '?':
			for m in process:
				cake[i][m] = last

		#This row is done.
		lastRow = cake[i]
		for m in perf:
			cake[m] = lastRow

		i+=1

	if isEmpty(cake[r-1]):
		for m in perf:
			cake[m] = lastRow

	print("Case #{}:".format(_+1))
	for row in cake:
		print(''.join(row))