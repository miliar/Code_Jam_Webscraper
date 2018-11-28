#!/usr/bin/python
def calculateTime(farmPrice, farmReward, total):
	cookieRate = 2
	farmCount = 0
	timeWithoutFarm = total/cookieRate
	bestTime = timeWithoutFarm
	farmBuyTime = 0

        while True:
		farmBuyTime = farmBuyTime + farmPrice/cookieRate
		catchupTime = total/(cookieRate + farmReward)
		timeWithFarm = farmBuyTime + catchupTime
		if (bestTime <  timeWithFarm) :
			return bestTime
		farmCount = farmCount + 1
		cookieRate = cookieRate + farmReward
		bestTime = timeWithFarm
 


def main() :
	fobj = open("input-cookie")
	writeobj = open("cookie-output.txt", 'w')
	caseNum = int(fobj.readline())
	print("No of cases is %d" %caseNum)
	for i in range (0, caseNum) :
		data = fobj.readline().split(" ")
		farmPrice = float(data[0])
		farmReward = float(data[1])
		total = float(data[2])
		timeAns = calculateTime(farmPrice, farmReward, total)
		writeobj.write("Case #%d: %.7f\n" %(i + 1, timeAns)) 

	writeobj.close()
	fobj.close()

main()
