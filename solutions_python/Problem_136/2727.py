f = open('data.in')
lines = f.readlines()
lines = [line.rstrip('\n') for line in open('data.in')]
output = open('output.in', 'w')

testCase = lines[0]
n = 0


while(n < int(testCase)):
	n+=1
	temp = lines[n].split()
	cost = float(temp[0])
	rate = float(temp[1])
	goal = float(temp[2])

	costTime = cost/2
	time = goal/2
	time2 = goal/(2+rate)
	timeFinal = time2+costTime
	buyNumber = 2

	while(timeFinal < time):
		costTime+=cost/(2+(buyNumber-1)*rate)
		time = timeFinal
		time2 = goal/(2+buyNumber*rate)
		timeFinal = time2+costTime
		buyNumber+=1
	
	print("Case #%s" % n + ":" + " %.7f" % time)
	output.write("Case #%s" % n + ":" + " %.7f" % time + "\n")
	
f.close()