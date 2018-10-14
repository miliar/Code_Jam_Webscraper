
testCases= raw_input()

for i in range(1,int(testCases)+1):
	inputStr = raw_input()
	input = []
	farmTime = []
	currentTime = []
	
	for x in inputStr.split(" "):
		input.append(float(x))
	
	
	mark = 0
	count = 0
	farmTime.append(0)
	cookieRate = 2
	
	while mark == 0:
		
		currentTime.append(farmTime[count] + (input[2]/cookieRate))
		#print currentTime[count]
		
		if currentTime[count]> currentTime[count-1] and count !=0:
			break			
		
		#print "cookie rate = " + str(cookieRate)
		farmTime.append(farmTime[count] + (input[0]/cookieRate))
		cookieRate = cookieRate + input[1]
		#print "Farm time " + str(count+1) + " = " + str(farmTime[count+1])
		count+=1
	
	print "Case #" + str(i) + ": " + str(currentTime[count-1])