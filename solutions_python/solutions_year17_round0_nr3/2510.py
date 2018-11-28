# Yash Mittal [yashmittal2009@gmail.com]


def getMaxPairs(arr, n):
    pairs = []

    start = True
    startIdx = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if not start:
                start = True
                startIdx = i
        else:
            if start:
                start = False
                pairs.append((startIdx, i - 1))
    if start:
        pairs.append((startIdx, n - 1))

    maxLen = 0
    countMax = 0
    maxPairs = []
    for pair in pairs:
        length = pair[1] - pair[0] + 1
        if length > maxLen:
            maxLen = length
            countMax = 1
            maxPairs = [pair]
        elif length == maxLen:
            countMax += 1
            maxPairs.append(pair)

    return maxPairs


def func(n, k):
	arr = [0] * n

	for i in range(k - 1):
	    maxPair = getMaxPairs(arr, n)[0]
	    mid = (maxPair[0] + maxPair[1]) // 2
	    arr[mid] = 1

  	maxPair = getMaxPairs(arr, n)[0]
  	mid = (maxPair[0] + maxPair[1]) // 2
  	left = mid - maxPair[0]
  	right = maxPair[1] - mid

  	return (right, left)

with open('C-small-1-attempt0.in', 'r') as fin:
    with open('output.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            line = fin.readline().strip().split(' ')
            lr, ls = func(int(line[0]), int(line[1]))
            fout.write('Case #{}: {} {}\n'.format(i, lr, ls))
