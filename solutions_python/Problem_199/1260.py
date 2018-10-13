import sys

[T, S, K, case_num] = [0, 0, 0, 0]

for line in sys.stdin:
	if T == 0:
		T = int(line.split('\n')[0])
	else:
		case_num += 1
		pancakeList = []
		[start, end, nflipCnt] = [1001, 1001, 0]
		S = line.split('\n')[0].split(' ')[0]
		K = int(line.split('\n')[0].split(' ')[1])
		listLength = len(S)
		for i in range(listLength):
			if S[i] == "+":
				pancakeList.append(1)
				if start > 0:
					start = i + 1
			else:
				pancakeList.append(-1)
				if start > 0:
					start = start * (-1)
				if end > 0:
					end = i + 1
				
		if start == listLength:
			print "Case #{0}: {1}".format(str(case_num), str(nflipCnt))
			continue
		start = max(1, start)
		end = min(listLength + 1, end)

		for i in range (start - 1, listLength-K+1):
			if pancakeList[i] > 0 and i > end:
				break
			if pancakeList[i] < 0:
				nflipCnt = nflipCnt + 1
				for j in range(0, K):
					pancakeList[i+j] = -1 * pancakeList[i+j]
		
		if sum(pancakeList[listLength - K: ]) != K:
			print "Case #{0}: {1}".format(str(case_num), "IMPOSSIBLE")
		else:
			print "Case #{0}: {1}".format(str(case_num), str(nflipCnt))