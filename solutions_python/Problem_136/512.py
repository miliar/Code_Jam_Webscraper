fin=open("B-large.in","r")
fout=open("output.txt","w")

cases=int(fin.readline())

for case in xrange(cases):
	case1Vals = fin.readline()
	c = float(case1Vals.split(" ")[0])
	f = float(case1Vals.split(" ")[1])
	x = float(case1Vals.split(" ")[2])
	
	currTime = x / 2
	farmBuildTime = 0

	farmI = 1
	while True:
		currFarmBuildTime = farmBuildTime + (c / ((farmI - 1) * f + 2))
		time = (x / (farmI * f + 2)) + currFarmBuildTime
		
		if time < currTime:
			currTime = time
			farmBuildTime = currFarmBuildTime
		else:
			break

		farmI += 1
	
	fout.write("Case #{0}: {1}\n".format(str(case + 1) , currTime))
fin.close()
fout.close()