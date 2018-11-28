

def poss(lawn, n, m):
	visited_col = [False]*m
	visited_row = [False]*n

	while True:

		ctr = 0
	#	print visited_row, " ", visited_col
		for i in range(n):
			if visited_row[i] == False:
				break
			else:
				ctr+=1
		ctr1 = 0
		if ctr == n:
			return True
		
		for i in range(m):
			if visited_col[i] == False:
				break
			else:
				ctr1+=1

		if ctr1 == m:
			return True

		ctr = 0
		ctr1 = 0

		min_row = None
		min_col = None
		min_elem = 100000
		for i in range(n):
			for j in range(m):
				if lawn[i][j] < min_elem and visited_row[i] == False and visited_col[j] == False:
					min_elem = lawn[i][j]
					min_row = i
					min_col = j

		ctr = 0
		for i in range(m):
			if visited_col[i] == True:
				ctr+=1
				continue
			if lawn[min_row][i] != min_elem:
				break
			else:
				ctr += 1
		check_row = False
		if ctr == m:
			check_row = True

		ctr = 0
		for i in range(n):
			if visited_row[i] == True:
				ctr+=1
				continue
			if lawn[i][min_col] != min_elem:
				break
			else:
				ctr += 1
		check_col = False
		if ctr == n:
			check_col = True


		if check_col:
			visited_col[min_col] = True
		elif check_row:
			visited_row[min_row] = True
		else:
			return False


	return False

n = int(raw_input())
for i in range(n):
	l = raw_input()
	l = l.split()
	n = int(l[0])
	m = int(l[1])
	lawn = [[None]*m for k in range(n)]
	for j in range(n):
		l = raw_input()
		l = l.split()
		for h in range(m):
			lawn[j][h] = int(l[h])


	if poss(lawn, n, m):
		print "Case #%d: YES" %(i+1)
	else:
		print "Case #%d: NO" %(i+1)

