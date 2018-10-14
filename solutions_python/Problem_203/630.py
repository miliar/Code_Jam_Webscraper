array = []
R = 0
C = 0

def solver():
	lastRowIsEmpty = True
	for i in range(R):
		if (not lastRowIsEmpty) and isEmptyRow(i):
			array[i] = array[i-1]
			lastRowIsEmpty = False
		else:
			array[i] = rowHelper(i)
			lastRowIsEmpty = isEmptyRow(i)

	lastRowIsEmpty = True
	for i in reversed(range(R)):
		if (not lastRowIsEmpty) and isEmptyRow(i):
			array[i] = array[i+1]
			lastRowIsEmpty = False
		else:
			array[i] = rowHelper(i)
			lastRowIsEmpty = isEmptyRow(i)


def rowHelper(row):
	tempArray = list(array[row])
	lastChar = '?'
	for i in range(C):
		if lastChar != "?" and tempArray[i] == "?":
			tempArray[i] = lastChar
		lastChar = tempArray[i]

	lastChar = '?'
	for i in reversed(range(C)):
		if lastChar != "?" and tempArray[i] == "?":
			tempArray[i] = lastChar
		lastChar = tempArray[i]

	return ''.join(map(str,tempArray))

def isEmptyRow(row):
	return array[row].count("?") == C


# def placeInGrid(sign, row, col):
# 	array[N * row + col] = sign
# 	return

# def getInGrid(row, col):
# 	return array[N * row + col]


# def validPoint(r,c):
# 	return (r >= 0 and r < N) and (c >= 0 and c < N)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	data = input().split(" ")
	array = []
	R = int(data[0])
	C = int(data[1])
	array = [None] * (R)
	for j in range(R):
		array[j] = input()
	solver()
	print("Case #{}:".format(i))
	for k in range(R):
		print(array[k])

