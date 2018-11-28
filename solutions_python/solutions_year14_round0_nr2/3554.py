iterations = 10000
baseCookieRate = 2.0


def parse(data):
	tokens = data.strip().split(' ')

	return {'C': float(tokens[0]),
			'F': float(tokens[1]),
			'X': float(tokens[2])}

def getFarmTime(farms, farmPrice, farmUpgradeRate):
	totalTime = 0.0
	cookieRate = baseCookieRate
	for i in range(farms):
		totalTime += farmPrice/cookieRate
		cookieRate += farmUpgradeRate

	return (totalTime, cookieRate)

def getMin(data):
	results = []
	previousTime = None;
	farmPrice = data['C']
	farmUpgradeRate = data['F']
	goal = data['X']
	for i in range(iterations):
		farms = i;
		#totalTime,cookieRate
		farmTime = getFarmTime(farms, farmPrice, farmUpgradeRate)
		xTime = goal/farmTime[1]

		totalTime = farmTime[0] + xTime
		if (previousTime == None):
			previousTime = totalTime
		elif (previousTime < totalTime):
			return previousTime
		else:
			previousTime = totalTime

		results.append(totalTime)

	#print(str(results).replace('[','').replace(']',''))
	return min(results)

count = int(raw_input(), 10)

data = []
for i in range(count):
	thisData = raw_input()
	data.append(parse(thisData))

for i in range(count):
	thisData = data[i]

	minimum = getMin(thisData)

	print("Case #" + str(i+1) + ": " + str(minimum))

