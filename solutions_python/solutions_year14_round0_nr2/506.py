T = int(raw_input())
for x in range(T):
	C,F,X = map(float,raw_input().split())

	baseRate = 2.0
	farmSum = 0.0
	answer = X/baseRate
	nextRate = baseRate
	while True:
		farmSum = farmSum + C/nextRate
		nextRate = nextRate + F
		nextTime = farmSum + X/nextRate
		if nextTime > answer:
			break
		else:
			answer = nextTime
	
	print "Case #"+str(x+1)+": "+str(answer)
