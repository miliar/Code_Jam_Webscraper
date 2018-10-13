#!/usr/bin/python

'''
Input				Output 
 
3 
---+-++- 3			Case #1: 3
+++++ 4				Case #2: 0
-+-+- 4				Case #3: IMPOSSIBLE


 
raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	print "Case #{}: {} {}".format(i, n + m, n * m)
	# check out .format's specification for more formatting options
			 

'''
numTest = int(raw_input()) # number of tests

# loop to print output
for i in xrange(1, numTest + 1):
	
	# grab each test case
	testCase = raw_input().split(" ")
	testNum = i
	scenario = testCase[0] # pancake scenario
	flipperLen = int(testCase[1]) # flipper size
	
	happy = "+"
	blank = "-"
	scenarioList = list(scenario)
	scenarioLen = len(scenarioList)
	
	flipCount = 0
	
	## CALCULATIONS
	# check for anything needs to be changed
	if blank not in scenarioList:
		print "Case #{}: {}".format(i, flipCount)
		continue
		#print "Easy"
	
	else:
		# loop through the whole scenario list	
		for j in xrange(scenarioLen):
			
			# flip mode as soon as you find a blank pancake
			# also check the boundary of the array
			if scenarioList[j] == blank and (j+flipperLen) <= scenarioLen:
				
				#print "J: ", j
				#print "Flipper Size: ", flipperLen
				#print "JFlipper: ", j+flipperLen
				#print "Before:", scenarioList
				
				# reversing pancakes
				for k in xrange(flipperLen):
					#print "J: {}, K: {}".format(j, k) 
					
					if scenarioList[ j+k ] == blank:
						scenarioList[ j+k ] = happy
						#print "After: ", scenarioList
					else:
						scenarioList[ j+k ] = blank
						#print "After: ", scenarioList
				flipCount += 1
		
		
	# evaluation			
	if blank not in scenarioList:
		print "Case #{}: {}".format(i, flipCount)
	else:
		print "Case #{}: {}".format(i, "IMPOSSIBLE")				



