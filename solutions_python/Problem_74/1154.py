import sys

def solve(data):
	parts = data.split(" ")
	length = parts[0]
	
	orangeParts = []
	blueParts = []
	
	for i in xrange(1, len(parts), 2):
		if parts[i] == 'B':
			blueParts.append(int(parts[i+1]))
			#print "Blue %d" % blueParts[-1]
		else:
			orangeParts.append(int(parts[i+1]))
			#print "Orange %d" % orangeParts[-1]

	orangePosition = 1
	bluePosition = 1
	time = 0
	
	blueCounter = 0
	orangeCounter = 0
	# Which color, position
	partsPos = 1
	waitUntil = [parts[partsPos], int(parts[partsPos+1])]
	#print waitUntil
	try: blueTarget = blueParts[blueCounter] 
	except: blueTarget = 1
	try: orangeTarget = orangeParts[orangeCounter] 
	except: orangeTarget = 1
		
	while (1):
		time += 1	
		#print " "
		#print "O%d B%d" % (orangePosition, bluePosition)
		#print "%s %d" % (waitUntil[0], waitUntil[1])
		#print " "
		
		#print "B%i" % bluePosition
		#print "O%i" % orangePosition

		if orangeTarget > orangePosition:		
			orangePosition += 1
			orangeAction = "UP"
		elif orangeTarget < orangePosition:
			orangePosition -= 1
			orangeAction = "DOWN"
		else:
			orangeAction = "PRESS"
		
		#print orangeAction
			
		if blueTarget > bluePosition:		
			bluePosition += 1
			blueAction = "UP"
		elif blueTarget < bluePosition:
			bluePosition -= 1
			blueAction = "DOWN"
		else:
			blueAction = "PRESS"

		#print blueAction

			# Press		
		if orangeAction == "PRESS" and waitUntil[0] == 'O' and orangePosition == waitUntil[1]:
			if orangeCounter != len(orangeParts)-1:
				orangeCounter += 1
				orangeTarget = orangeParts[orangeCounter]
			partsPos += 2
			if partsPos >= len(parts):
				#print "YEY"
				break
			waitUntil = [parts[partsPos], int(parts[partsPos+1])]			
			
		elif blueAction == "PRESS" and waitUntil[0] == 'B' and bluePosition == waitUntil[1]:
			if blueCounter != len(blueParts)-1:
				blueCounter += 1
				blueTarget = blueParts[blueCounter]
			partsPos += 2
			if partsPos >= len(parts):
				#print "YEY"	
				break
			waitUntil = [parts[partsPos], int(parts[partsPos+1])]

	return time
		
fd = open(sys.argv[1], "r")
inputs = int(fd.readline()[:-1])

for i in xrange(inputs):
	line = fd.readline()[:-1]
	
	res = solve(line)
		
	#print line
	print "Case #%d: %d" % (i+1, res)
	#print ""
		
	