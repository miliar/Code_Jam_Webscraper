T = int(raw_input())

currentTestCase = 1
while currentTestCase <= T:
	N = raw_input()
	intN = int(N)
	tidy = 0
	
	while tidy == 0:
	
		if int(N) < 10:
			tidy = 1
			print "Case #",currentTestCase,": ",N 
		else:
			numberOfPotenses = len(N)-1
			i = 0
			while i < numberOfPotenses:
				if N[i] <= N[i+1]:
					i += 1
					tidy = 1
				else:
					tidy = 0
					break
			if tidy == 1:
				print "Case #",currentTestCase,": ",intN 
			else:
				intN -= 1
				N = str(intN)
				
	currentTestCase += 1