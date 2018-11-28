infile = open("B-large.in",'r')
outfile = open("b.out",'w')

def CPS(numFarms, f):
	return 2 + numFarms * f

def timeForX(cps, x):
	return x / cps

numCases = int(infile.readline())
for i in range(numCases):
	line = infile.readline()
	line = line.split(" ")
	c,f,x = float(line[0]),float(line[1]),float(line[2])
	numFarms = 0
	cps = 2
	time = timeForX(cps, x)
	#print("Takes {0} seconds to get {1} cookies, going at {2} cps with {3} farms".format(time, x, cps, numFarms))
	times = []
	times.append(time)
	previousFarmcost = 0
	optimized = False
	while not optimized:
		farmcost = c/(cps)
		totalFarmcost = farmcost + previousFarmcost
		numFarms += 1
		cps = CPS(numFarms, f)
		#print("Costs {0} to buy 1 additional farm, up to {1} farms going at {2} cps. Total time spent on farms: {3}".format(farmcost, numFarms, cps, totalFarmcost))
		time = timeForX(cps, x)
		#print("It now takes {0} seconds to get {1} cookies, going at {2} cps with {3} farms".format(time, x, cps, numFarms))
		totaltime = totalFarmcost + time
		#print("total time: {0}".format(totaltime))
		times.append(totaltime)
		
		if times[numFarms - 1] < times[numFarms]:
			optimized = True
		previousFarmcost = totalFarmcost
		
		#print(times[-2:], optimized)
		
		#input()

	outfile.write("Case #{0}: {1:.7f}\n".format(i+1,times[numFarms - 1]))