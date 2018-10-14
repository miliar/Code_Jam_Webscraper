import fileinput


if __name__ == "__main__":
	
	f = fileinput.input()

	T = int(f.readline())

	for case in range(1, T+1):

		L = f.readline().strip('\n')
		N = int(L.split(' ')[0])
		K = int(L.split(' ')[1])
		#print "N: " + str(N) + "  K: "+ str(K) 

		storeDict = {}
		storeDict[N] = 1
		#print "storeDict: " + str(storeDict)

		for i in range(0,K-1):
			num = max(storeDict.keys(), key = int)
			#print "num: " + str(num)
			if storeDict[num] > 1: 
				storeDict[num] -= 1
			
			else:
				storeDict.pop(num, None)
		
			#print "storeDict: " + str(storeDict)

			num1 = num/2

			#if num1 == -1:
				#print "num: " + str(num)+ "  num1: " + str(num1)
			#print "num1: "+ str(num1) + "  num2: "+ str(num2)
		
			for j in range(2):
				if num1 in storeDict:
					storeDict[num1] += 1
				else:
					storeDict[num1] = 1

				if num%2 == 0:
					num1 = num/2 - 1
				
		
			#print "storeDict: " + str(storeDict)


		#the last people 
		lastPeopleNum = max(storeDict.keys(), key = int)
		storeMin = 0
		storeMax = 0

		if lastPeopleNum%2 == 0:
			storeMin = lastPeopleNum/2 - 1
			storeMax = lastPeopleNum/2 
		else:
			storeMin = (lastPeopleNum - 1)/2
			storeMax = (lastPeopleNum - 1)/2
		
		outStr = str(storeMax) + " " + str(storeMin) 
			



		print("Case #{0}: {1}".format(case, outStr))
