def flipPancake(pancakes, index, k):
	for i in range(k):
		if pancakes[index+i] == "-":
			pancakes[index+i] = "+"
		else:
			pancakes[index+i] = "-"
	return pancakes

def doWork(pancakes, k):
	count = 0
	for j in range(len(pancakes)):
		if pancakes[j] == "-":
			if j > len(pancakes)-k:
				return "IMPOSSIBLE"
				break
			pancakes = flipPancake(pancakes, j, k)
			count += 1
	return count

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inputArray = [s for s in raw_input().split(" ")]
    pancakes = list(inputArray[0])
    k = int(inputArray[1])
    print "Case #{}: {}".format(i, doWork(pancakes, k))
