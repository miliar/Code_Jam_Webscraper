def alphabetCake(l, r, c, x):
	for i in range(x, r):
		empty = 0
		while empty < c and not l[i][empty]:
			empty += 1
		if empty < c:
			current = l[i][empty]
		else:
			current = 0
		for j in range(empty):
			l[i][j] = current
		for j in range(c):
			if not l[i][j]:
				l[i][j] = current
			else:
				current = l[i][j]
	current = l[x]
	for i in range(r):
		if allEmpty(l[i]):
			l[i] = current
		else:
			current = l[i]
		i += 1
	return l

def allEmpty(lst):
	for i in lst:
		if i != 0:
			return False
	return True






t = int(input())
for i in range(1, t+1):
	row, column = map(int, input().split(" "))
	biglst = []
	for j in range(row):
		smalllst = []
		current = input()
		for k in range(len(current)):
			if current[k] == '?':
				smalllst += [0]
			else:
				smalllst += [current[k]]
		biglst += [smalllst]
	x = 0
	for j in range(row):
		if allEmpty(biglst[j]):
			x = j + 1
		else:
			break
	answer = alphabetCake(biglst, row, column, x)
	print("Case #{}: ".format(i))
	for j in range(row):
		str1 = ''.join(answer[j])
		print(str1)


