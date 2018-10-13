def getMaxMin(stalls):
	index = 0
	bestMin = 0
	bestMax = 0
	for i in range(1,len(stalls)-1):
		(x, y) = stalls[i]
		(x, y) = (max(i-x, y-i-1), min(i-x, y-i-1))
		if (y > bestMin or y == bestMin and x > bestMax): 
			index = i
			bestMin, bestMax = y, x
	return (index, bestMax, bestMin)

def adjustSpace(stalls, index):
	stalls[index] = (-1, -1)
	for i in range(1, len(stalls)-1):
		(x, y) = stalls[i]
		if (i < index and y >= index): #adjust original right boundary
			stalls[i] = (x, index)
		elif (i > index and x <= index):
			stalls[i] = (index+1, y)
	return stalls

T = int(raw_input())
for i in xrange(1, T+1):
	n, k = [int(x) for x in raw_input().split(" ")]

	stalls = [None] * (n+2)
	stalls[0] = stalls[-1] = (-1, -1)
	for j in xrange(1, n+1):
		stalls[j] = (1, n+1) #leftmost, rightmost indices
	for p in xrange(k-1):
		(index, bmi, bmx) = getMaxMin(stalls)
		stalls = adjustSpace(stalls, index)

	(index, bmi, bmx) = getMaxMin(stalls)

	print "Case #{}: {} {}".format(i, bmi, bmx)