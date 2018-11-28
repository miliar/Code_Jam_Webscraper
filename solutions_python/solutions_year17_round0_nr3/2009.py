import bisect


def doCase(N, K):
	frontier = [N]
	for k in range(K):
		biggestFree = frontier.pop() - 1
		if biggestFree%2 == 0:
			lastMin = int(biggestFree/2)
			lastMax = int(biggestFree/2) 
			bisect.insort(frontier, lastMax) 
			bisect.insort(frontier, lastMin)
		else:
			lastMin = int((biggestFree - 1) / 2)
			lastMax = int((biggestFree + 1) / 2) 
			bisect.insort(frontier, lastMax) 
			bisect.insort(frontier, lastMin)
	return lastMax, lastMin

T = int(input())
for i in range(1, T + 1):
	N, K = [int(s) for s in input().split(" ")]
	lrmax, lrmin = doCase(N, K)
	print("Case #{}: {} {}".format(i, lrmax, lrmin))
