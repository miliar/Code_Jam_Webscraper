T = int(raw_input())

for t in range(T):
	R,C = map(lambda x: int(x), raw_input().split(" "))
	arr = []

	total_blue = 0
	for i in range(R):
		arr.append(list(raw_input()))
		total_blue += arr[-1].count('#')

	for i in range(R-1):
		for j in range(C-1):
			if arr[i][j] == '#':
				if arr[i][j+1] == '#' and arr[i+1][j] == '#' and arr[i+1][j+1] == '#':
					arr[i][j] = "/"
					arr[i][j+1] = "\\"
					arr[i+1][j] = "\\"
					arr[i+1][j+1] = "/"

					total_blue -= 4
	print "Case #%d:" % (t+1)
	if total_blue != 0:	
		print "Impossible"
	else:
		for i in range(R):
			print "".join(arr[i])
		