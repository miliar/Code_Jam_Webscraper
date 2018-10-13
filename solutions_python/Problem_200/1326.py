import sys
import math

[T, N, case_num] = [0, 0, 0]

for line in sys.stdin:
	if T == 0:
		T = int(line.split('\n')[0])
	else:
		case_num += 1
		N = int(line.split('\n')[0])
		currentList = map(int, str(N))
		
		rightSmallest = currentList[len(currentList) - 1]
		
		for i in range(len(currentList) - 1, 0, -1):
			leftBiggest = 0

			for j in range(0, i):
				if currentList[j] > leftBiggest:
					leftBiggest = currentList[j]
			if currentList[i] < leftBiggest:
				#N = N - (currentList[i])*(pow(10, (len(currentList) - i - 1))) - 1
				for k in range(i, len(currentList)):
					currentList[k] = 9
				currentList[i-1] = currentList[i-1] - 1

		print "Case #{0}: {1}".format(str(case_num),  int(''.join(map(str, currentList))))