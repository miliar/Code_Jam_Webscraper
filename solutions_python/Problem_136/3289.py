cookieFarmCost = 0
cookieFarmProduction = 0
spentCookies = 0
balance = 0
goal = 0

curSecondsToWin = 0
withAnotherFarm = 0
curCookiesSecond = 2
timeTillNextFarm = 0

fin = file("large.in")
fout = file("ex.out", "w")
for i in range(0,int(fin.readline())):
	data = map(float, fin.readline().split(' '))
	farmCost = data[0]
	farmProduction = data[1]
	goal = data[2]
	cps = 2
	timeElapsed = 0
	#time left with current rate of cps
	curTime = goal/cps
	#time left if we wait for another farm
	withAnotherFarm = farmCost/cps+goal/(cps+farmProduction)
	while withAnotherFarm < curTime:
		timeElapsed += farmCost/cps
		cps += farmProduction
		curTime = goal/cps
		withAnotherFarm = farmCost/cps+goal/(cps+farmProduction)
	fout.write("Case #"+str(i+1)+": "+str(timeElapsed+curTime)+"\n")

