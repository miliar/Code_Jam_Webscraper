#Open the file
filename = 'B-large.in' 
fin=open(filename,'r')

#First file input is the number of cases

input = fin.readline()
totalLines = int(input)

#Loop and do all problems

for i in range(0,totalLines):

	#Read in all values first
	input = fin.readline()
	input = input.strip().split()		
	tempVal = [float(j) for j in input]
	
	farmCost=tempVal.pop(0)
	rateBoost=tempVal.pop(0)
	winCost=tempVal.pop(0)

	#Start things at zero
	FinishTotal=0.00
	FarmTotal=0.00
	newFinish=0.00

	#Now the fun part!

	solved = 0
	currentRate=2.0	#HARD CODED START RATE 2
	while solved == 0:
		
		#Compute Time to finish, farm
		FinishTotal = FarmTotal + (winCost/currentRate)
		FarmTotal = FarmTotal + (farmCost/currentRate)

		#Check the new things
		currentRate = currentRate + rateBoost
		newFinish = FarmTotal + (winCost/currentRate)
		
		if (newFinish > FinishTotal):
			solved = 1
	print("Case #%d: %.7f" %((i+1), FinishTotal))
