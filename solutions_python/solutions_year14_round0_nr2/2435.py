T = int(raw_input())


def takesTime(start, goal, rate):
	return (goal - start) / rate

for i in range(1, T+1):

	CFX = [float(elem) for elem in raw_input().replace('\n', '').split()]
	
	C = CFX[0]
	F = CFX[1]
	X = CFX[2]

	time = 0
	rate = 2
	cookies = 0
	
	while True:
		
		timeToBuyFactory = takesTime(0, C, rate)
		timeAfterBuyingFactory = takesTime(0, X, rate + F) + timeToBuyFactory
		timeJustWaiting = takesTime(0, X, rate)
		
		if timeAfterBuyingFactory < timeJustWaiting:
			time += timeToBuyFactory
			rate = rate+F
		else:
			time += timeJustWaiting
			break

	print "Case #"+str(i)+": " + str(time)