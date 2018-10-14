#Open the file
filename = 'A-small-attempt0.in' 
fin=open(filename,'r')

#First filename input is the number of tricks

input = fin.readline()
testCases = int(input)

#Go for all test cases

for i in range(0,testCases):

	input = fin.readline()
	tempVal = [str(j) for j in input]

	maxShyness=int(tempVal.pop(0))
	crapSpace=tempVal.pop(0)
	#audienceMakeupString=str(tempVal)

	#Initialize Current Number standing to 0
	curStanding=0

	#Initialize Shyness Level to be standing to 0
	shyLevel=0

	#Initialize Friends Added to 0
	friendsAdded=0

	while shyLevel <= maxShyness:

		numAtLevel = int(tempVal.pop(0))
		if (curStanding < shyLevel)and(numAtLevel>0):
			friendsAdded += (shyLevel-curStanding)
			curStanding += (shyLevel-curStanding)
		curStanding += numAtLevel
		shyLevel+=1
	
	print("Case #%d: %d" %((i+1), friendsAdded))




