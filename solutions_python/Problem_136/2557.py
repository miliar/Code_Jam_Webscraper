import sys
f = open("B-large.in")
o = open("B-large.out", "w")
T = int(f.readline())
for t in range(T):
	data = f.readline().split(" ")
	C = float(data[0])
	F = float(data[1])
	X = float(data[2])
	buy = True
	timeSpentUpgrading = 0
	P = 2
	while buy == True:
		buy = False
		time = X/P + timeSpentUpgrading
		#print("Time:" + str(time))
		#If buy
		timeToBuy = C/P
		#print("timeToBuy:" + str(timeToBuy))
		timeSpentUpgrading += timeToBuy
		#print("Upgrade:" + str(timeSpentUpgrading))
		pAfterBuy = P+F
		#print("pAfterBuy:" + str(pAfterBuy))
		timeToGoal = X/pAfterBuy
		#print("timeToGoal:" + str(timeToGoal))
		if timeToGoal+timeSpentUpgrading < time:
			buy = True
			P += F
		else:
			break
	o.write("Case #" + str(t+1) + ": " + "{:.7f}".format(time) + "\n")