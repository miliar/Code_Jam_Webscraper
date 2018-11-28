from queue import Queue

# tuple goes into it {pattern: depth}
touchedNodes = {}
tempQueue = Queue()

def solver(pancakes,size):
	touchedNodes[pancakes] = 0
	tempQueue.put_nowait((pancakes,0))
	minLen = -1
	while not tempQueue.empty():
		temp = helper(size)
		if minLen != -1:
			if temp < minLen and temp != -1:
				minLen = temp
		else:
			minLen = temp

	# after
	target = generateFinalString(pancakes)

	if target in touchedNodes:
		return str(touchedNodes[target])
	else:
		return 'IMPOSSIBLE';	

def helper(size):
	node = tempQueue.get_nowait()
	depth = node[1]
	pancakes = node[0]
	# print(pancakes + ' ' + str(depth))
	# base case
	if '-' not in pancakes:
		return depth

	numBranches = len(pancakes) - size + 1
	
	for i in range(numBranches):
		flipped = flip(pancakes,size,i)
		curDepth = depth + 1
		if flipped in touchedNodes: # if exists, update and stop
			if curDepth < touchedNodes[flipped]:
				touchedNodes[flipped] = curDepth
		else: # if not exist, continue
			touchedNodes[flipped] = curDepth
			tempQueue.put_nowait((flipped,curDepth))
	return -1

		

def flip(pancakes, size, startIdx):
	flipped = pancakes[0:startIdx]
	for i in range(size):
		if pancakes[i+startIdx] == '+':
			flipped = flipped + '-'
		else:
			flipped = flipped + '+'

	return flipped + pancakes[startIdx+size:]


def elemExist(arr,target):
	return target in arr

def generateFinalString(pancakes):
	retVal = ''
	for i in pancakes:
		retVal = retVal + '+'
	return retVal

# pancakes = '-++++++++-'
# print (solver(pancakes,2))


# touchedNodes = {}
# pancakes2 = '----------'
# print (solver(pancakes2,2))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	data = input().split(" ")
	pancakes = data[0]
	size = data[1]
	touchedNodes = {}
	tempQueue = Queue()
	print("Case #{}: {}".format(i, solver(pancakes, int(size))))