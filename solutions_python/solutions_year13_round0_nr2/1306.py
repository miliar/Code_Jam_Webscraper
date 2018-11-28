T = int(raw_input())
for t in range(T):
	n,m = map(int,raw_input().strip().split(' '))
	table = []
	for i in range(n):
		temp = map(int,raw_input().strip().split(' '))
		table.append(temp)
	count = [[0 for i in range(m)] for i in range(n)]
	for i in range(n):
		_max = max(table[i])
		for j in range(m):
			if(table[i][j] < _max):
				count[i][j] += 1
	for i in range(m):
		temp = []
		for j in range(n):
			temp.append(table[j][i])
		_max = max(temp)
		for j in range(n):
			if(table[j][i] < _max):
				count[j][i] += 1
	#print count
	check_answer = True
	for i in range(n):
		for j in range(m):
			if(count[i][j] == 2):
				check_answer = False
	print 'Case #' + str(t+1) + ':',
	if(check_answer):
		print 'YES'
	else:
		print 'NO'
