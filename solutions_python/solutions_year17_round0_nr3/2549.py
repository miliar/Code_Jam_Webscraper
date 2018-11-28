#author : ash=ishh..

T = int(input())

for case in range(T):
	N,K = input().split()
	N = int(N)
	K = int(K)
	stalls = []

	stalls.append(1)
	for i in range(N):
		stalls.append(0)
	stalls.append(1)


	for person in range(K):
		leftright = []
		for i in range(N+2):
			leftright.append((-1,-1))
		

		for each in range(1,len(stalls)-1):
			if stalls[each] == 0: 
				left = 0
				right = 0
				for l in range(each-1,0,-1):
					if stalls[l] == 1:
						break
					else:
						left += 1
				for r in range(each+1,len(stalls)-1):
					if stalls[r] == 1:
						break
					else:
						right += 1
				leftright[each] = (left,right)	

		minindex = 1
		minans = min(leftright[1])
		maxans = max(leftright[1])

		for index in range(2,len(leftright)):
			if(min(leftright[index]) > minans):
				minans = min(leftright[index])
				maxans = max(leftright[index])
				minindex = index
			elif(min(leftright[index]) == minans):
				if(max(leftright[index]) > maxans):
					minans = min(leftright[index])
					maxans = max(leftright[index])
					minindex = index 
		stalls[minindex] = 1
	print("Case #{}: {} {}".format(case+1,leftright[minindex][1],leftright[minindex][0]))
