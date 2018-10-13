from sys import stdin, setrecursionlimit

setrecursionlimit(2000)


def possible(colors):
	N = sum(colors)
	max_single_color = (N + 1) / 2
	R,O,Y,G,B,V = colors
	if R + O + V > max_single_color:
		return False
	if O + Y + G > max_single_color:
		return False
	if G + B + V > max_single_color:
		return False
	return True

def compatible(c1, c2):
	colorCount = [0] * 6
	colorCount[c1] += 1
	colorCount[c2] += 1
	return possible( tuple(colorCount) )


colorDict = ['R', 'O', 'Y', 'G', 'B', 'V']

def getOrdering(first, end, colors, order):
	# base case
	N = sum(colors)
	if N == 0:
		if not compatible(first, end):
			return None
		return order
	
	if N == 1:
		remainingColorIndex = filter(lambda i: colors[i] > 0, range(6))[0]
		return getOrdering(first, remainingColorIndex, (0,0,0,0,0,0), order + colorDict[remainingColorIndex])

	if not possible(colors):
		return None

	for i in range(6):
		if colors[i] > 0 and compatible(i, end):
			newColors = list(colors)
			newColors[i] -= 1
			ret_order = getOrdering(first, i, tuple(newColors), order + colorDict[i])
			if ret_order != None:
				return ret_order

	return None

def getOrderingHelper(colors):
	index = -1
	for i in range(6):
		if colors[i] > 0:
			index = i
			break
	newColors = list(colors)
	newColors[i] -= 1
	order = getOrdering(index, index, tuple(newColors), colorDict[index])
	if order == None:
		return 'IMPOSSIBLE'
	return order

with open('B-small-attempt1.in', 'r') as f:

	T = int(f.readline())

	for caseNum in range(T):
		N, R, O, Y, G, B, V = map(int, f.readline().strip().split())
		colors = (R,O,Y,G,B,V)
		print 'Case #%d: %s' %(caseNum + 1, getOrderingHelper(colors))

	

