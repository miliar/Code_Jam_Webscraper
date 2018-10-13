import sys
tests = int(raw_input())
for case in range(tests):
	d = dict()
	arr = map(int, raw_input().split())
	rows = arr[0]
	cols = arr[1]
	matrix = []
	for i in range(rows):
		matrix.append(list(raw_input()))
	set1 = set()
	for i in range(rows):
		for j in range(cols):
			if matrix[i][j] != '?' and not (matrix[i][j] in set1):
				set1.add(matrix[i][j])
	for letter in set1:
		leftTop = [rows, cols]
		rightBottom = [-1, -1]
		for i in range(rows):
			for j in range(cols):
				if matrix[i][j] == letter:
					if leftTop[0] > i:
						leftTop[0] = i
					if leftTop[1] > j:
						leftTop[1] = j
					if rightBottom[0] < i:
						rightBottom[0] = i
					if rightBottom[1] < j:
						rightBottom[1] = j
		for i in range(leftTop[0], rightBottom[0]+1):
			for j in range(leftTop[1],rightBottom[1]+1):
				matrix[i][j] = letter
		d[letter] = [leftTop,rightBottom]
	
	for letter in set1:
		leftTop = d[letter][0]
		rightBottom = d[letter][1]
		rightTop = [leftTop[0],rightBottom[1]]
		leftBottom = [rightBottom[0],leftTop[1]]
		found = False
		while not found and rightTop[1] < cols-1:
			for i in range(rightTop[0],rightBottom[0]+1):
				j = rightTop[1] + 1
				if matrix[i][j] != '?':
					found = True
					break
			if found:
				break
			for i in range(rightTop[0],rightBottom[0]+1):
				j = rightTop[1] + 1
				matrix[i][j] = letter
			rightTop[1] += 1
			rightBottom[1] += 1
		
		found = False
		while not found and leftTop[1] > 0:
			for i in range(leftTop[0],leftBottom[0]+1):
				j = leftTop[1] - 1
				if matrix[i][j] != '?':
					found = True
					break
			if found:
				break
			for i in range(leftTop[0],leftBottom[0]+1):
				j = leftTop[1] - 1
				matrix[i][j] = letter
			leftTop[1] -= 1
			leftBottom[1] -= 1
		
		found = False
		while not found and leftTop[0] > 0:
			for j in range(leftTop[1],rightTop[1]+1):
				i = leftTop[0] - 1
				if matrix[i][j] != '?':
					found = True
					break
			if found:
				break
			for j in range(leftTop[1],rightTop[1]+1):
				i = leftTop[0] - 1
				matrix[i][j] = letter
			leftTop[0] -= 1
			rightTop[0] -= 1
		
		found = False
		while not found and leftBottom[0] < rows-1:
			for j in range(leftBottom[1],rightBottom[1]+1):
				i = leftBottom[0] + 1
				if matrix[i][j] != '?':
					found = True
					break
			if found:
				break
			for j in range(leftBottom[1],rightBottom[1]+1):
				i = leftBottom[0] + 1
				matrix[i][j] = letter
			leftBottom[0] += 1
			rightBottom[0] += 1
	
	print "Case #" + str(case+1) + ":"
	for i in range(rows):
		for j in range(cols):
			sys.stdout.write(str(matrix[i][j]))
		print ""