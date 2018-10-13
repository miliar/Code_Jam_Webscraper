import sys
import math

[T, N, K, case_num] = [0, 0, 0, 0]

for line in sys.stdin:
	if T == 0:
		T = int(line.split('\n')[0])
	else:
		case_num += 1
		N = int(line.split('\n')[0].split(" ")[0]) # number of bathroom
		K = int(line.split('\n')[0].split(" ")[1]) # number of person
		#bath = [N]
		layer = int(math.log(K,2))
		beforeLastPersonInLastLayerCnt = K - pow(2,layer)
		bathList = [{N:1}]
		cnt = 0

		for i in range(1, layer + 1):
			currentBath = {}
			for emptySection in bathList[i-1]:
				div = [int(math.ceil((emptySection - 1.0)/2)), int(math.floor((emptySection - 1.0)/2))]
				
				for size in div:
					if size in currentBath:
						currentBath[size] = currentBath[size] + bathList[i-1][emptySection]
					else:
						currentBath[size] = bathList[i-1][emptySection]
			bathList.append(currentBath)
	
		keylist = reversed(sorted(bathList[layer]))

		for key in keylist:
			cnt = cnt + bathList[layer][key]
			if cnt > beforeLastPersonInLastLayerCnt:
				room = (key - 1.0) / 2
				print "Case #{0}: {1} {2}".format(case_num, int(math.ceil(room)), int(math.floor(room)))
				break