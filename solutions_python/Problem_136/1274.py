

def main():
	f = file("data.txt")
	numberOfCases = int(f.readline().rstrip())
	for case in xrange(0,numberOfCases):
		rawData = [float(x) for x in f.readline().rstrip().split()]
		farmCost = rawData[0]
		farmProductionRate = rawData[1]
		finishLine = rawData[2]
		currentProductionRate = 2.0
		timeElapsed = 0
		cookies = 0

		while cookies < finishLine:
			timeTilFarm = farmCost / currentProductionRate
			timeTilFinish = (finishLine - cookies) / currentProductionRate
			if timeTilFinish < timeTilFarm:
				timeElapsed += timeTilFinish
				break
			else:				
				timeElapsed += timeTilFarm
				cookies += timeTilFarm * currentProductionRate
				possibleProductionRate = currentProductionRate + farmProductionRate
				possibleTimeElapsed = (finishLine - (cookies - farmCost)) / possibleProductionRate
				currentProductionTime = (finishLine - cookies) / currentProductionRate

				if currentProductionTime > possibleTimeElapsed:
					currentProductionRate = possibleProductionRate
					cookies -= farmCost
				#print cookies
		print "Case #%i: %f" % (case + 1, timeElapsed)

if __name__ == '__main__':
	main()