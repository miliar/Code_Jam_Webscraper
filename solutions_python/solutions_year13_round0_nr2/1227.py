def getMinHeight(arr,n,m):
	minHeightX = min(arr[0])
	minHeightY = min(arr[y][0] for y in range(n))

	print minHeightX,minHeightY

	minHeight = min(minHeightY,minHeightX)
	return minHeight


def processArr(arr,n,m):
	for y in xrange(n):

		maxHeight = max(arr[y])
		for x in xrange(m):
			if arr[y][x] != maxHeight:
				for otherY in xrange(n):
					if arr[otherY][x] > arr[y][x]:
						return "NO"

	return "YES"






with open('input','r') as fileIn:
	with open('output','w') as fileOut:

		cases = int(fileIn.readline())

		for cas in xrange(cases):
			nextLine = fileIn.readline().split()
			n = int(nextLine[0])
			m = int(nextLine[1])

			arr = [ [] for _ in xrange(n)]

			for y in range(n):
				line = fileIn.readline().split()
				for x in range(m):
					arr[y].append(int(line[x]))

			result = "Case #%d: %s" % (cas+1,processArr(arr,n,m))

			print result
			fileOut.write(result + '\n')