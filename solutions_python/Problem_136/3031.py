#!/usr/bin/python

# Read Input
fname = "B-large.in"
#fname = "B-small-attempt1.in"
#fname = "B_small.txt"
FileContent = []
with open(fname) as f:
	FileContent = f.readlines()
	
# First line = number of test cases
NumCases = int(FileContent[0])

		
# Main function
i = 1
for t in range(1,NumCases+1):
	
	CPS = 2.0 # Starting Cookies per second
	
	# Read each test case
	Case = FileContent[i].split()
	i += 1

	# Split Values
	FarmCost = float(Case[0])
	FarmGain = float(Case[1])
	Goal = float(Case[2])
	
	#print FarmCost, FarmGain, Goal
	#totalSec = CalcStrategy(FarmCost, FarmGain, Goal, CPS, 0.0)
	
	totalSec = 0.0
	while True:
		option1 = Goal / CPS
		option2 = (FarmCost / CPS) + (Goal / (CPS+FarmGain))
		if option1 <= option2:
			totalSec += option1
			break
		else:
			totalSec += (FarmCost / CPS)
			CPS += FarmGain
	
	Answer = round(totalSec,7)
	
	# Output!
	output = "Case #%d: %.7f" % (t, Answer)
	print output