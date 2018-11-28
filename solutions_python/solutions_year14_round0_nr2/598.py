import os

t = int(input())
for ti in range(1, t+1):
	line = input().split()
	rate = 2.0
	cookies = 0.0
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	t = 0.0
	#print ( str(c) + " " + str(f) + " " + str(x) )

	while(1):
		timeToFinish1 = x/rate

		timeToBuyFarm = c/rate
		newRate = rate + f
		timeToFinish2 = x/newRate + timeToBuyFarm
		if (timeToFinish1 < timeToFinish2):
			t += timeToFinish1
			print("Case #" + str(ti) + ": " + str(t))
			break
		else:
			t += timeToBuyFarm
			rate = newRate
			cookies = 0




