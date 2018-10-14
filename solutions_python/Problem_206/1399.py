import fileinput


def analysisHorseData(distance,horseData):
	timeList = []
	for data in horseData: 
		time = (distance - data[0])*1.0/data[1]*1.0
		timeList.append(time)

	maxTime = max(timeList)
	return format(distance*1.0/maxTime*1.0, '.6f')
	#print "timeList: " + str(timeList)




if __name__ == "__main__":
	
	f = fileinput.input()

	T = int(f.readline())

	for case in range(1, T+1):
		L = f.readline().strip('\n').split(' ')
		D = int(L[0])
		N = int(L[1]) 


		horseData = []
		for i in range(0, N):
			L = f.readline().strip('\n').split(' ')
			K = int(L[0])
			S = int(L[1]) 
			horseData.append((K,S)) 

		outStr = analysisHorseData(D,horseData)

		#print "horseData: " + str(horseData)

		print("Case #{0}: {1}".format(case, outStr))
