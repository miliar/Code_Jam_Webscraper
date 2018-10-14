import sys

filename = "B-large"

def solve_case(farmCost, farmRate, goal):
	time = 0.0
	rate = 2.0
	if goal < farmCost:
		return goal / rate
	while(True):
		timeToNextFarm = farmCost / rate
		timeToWin = goal / rate
		timeToWinWithFarmPurchase = timeToNextFarm + goal / (rate + farmRate)
		if timeToWinWithFarmPurchase < timeToWin:
			time += timeToNextFarm
			rate += farmRate
		else:
			return time + timeToWin

	output = time
	return ret

def readInt(inFile):
	return int(inFile.readline())

def readFloats(inFile):
	return [float(n) for n in inFile.readline().split(" ")]

def readInts(inFile):
	return [int(n) for n in inFile.readline().split(" ")]

with open(filename + ".in", 'r') as inFile:
	output_data = []

	# parse input
	T = readInt(inFile)
	for t in range(T):
		floats = readFloats(inFile)
		soln = solve_case(floats[0], floats[1], floats[2])
		output_data.append("Case #%s: %1.7f" % (t+1, soln))

	if len(output_data) > 0:
		with open(filename + ".out", 'w') as outFile:
			outFile.write("\n".join(output_data))
	else:
		print("no output")




