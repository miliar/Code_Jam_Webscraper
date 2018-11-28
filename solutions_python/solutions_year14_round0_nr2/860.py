inp = open("B-large.in", "r")
testcase=int(inp.readline())
# print testcase

out = open("./largeout.txt", "w")

for i in xrange(testcase):
	c, f, x=[float(temp) for temp in (inp.readline()).split(" ")]

	totalBuildTime=0
	speed=2
	timeAtThisSpeed=x*1.0/speed
	timeAtNextSpeed=x*1.0/(speed+f)
	buildTime=c*1.0/speed

	while buildTime+timeAtNextSpeed<timeAtThisSpeed:
		totalBuildTime+=buildTime
		speed+=f
		timeAtThisSpeed=x*1.0/speed
		timeAtNextSpeed=x*1.0/(speed+f)
		buildTime=c*1.0/speed

	result=("%.7f" % (totalBuildTime+timeAtThisSpeed))
	result= "Case #"+str(i+1)+": "+str(result)
	out.write(result+"\n")

out.close()
