import re

def checkTidy(inputNArray):
	lastSeen = None
	for digit in inputNArray:
		if lastSeen is None:
			lastSeen = int(digit)
		else:
			if lastSeen > int(digit):
				return False
			lastSeen = int(digit)
	return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inputArray = [int(s) for s in raw_input().split(" ")]
    inputN = inputArray[0]
    if inputN < 10:
    	print "Case #{}: {}".format(i, inputN)
    else:
    	while inputN > 0:
    		if re.match('1+0+', str(inputN)):
    			length = len(str(inputN))
    			tidy = "9" * (length-1)
    			print "Case #{}: {}".format(i, tidy)
    			break    			
    		inputNArray = list(str(inputN))
    		if checkTidy(inputNArray):
    			print "Case #{}: {}".format(i, inputN)
    			break
    		else:
        		inputN -= 1


  # print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options

