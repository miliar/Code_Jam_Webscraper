rowCountConstant = 4

#Open the file
filename = 'A-small-attempt0.in' 
fin=open(filename,'r')

#First filename input is the number of tricks

input = fin.readline()
trickCount = int(input)

#Go until we're out of tricks

for i in range(0,trickCount):
	
	input = fin.readline()
	firstRowNumber = int(input)
	#We only care about the values in this row
	#4 rows every time

	curRow=0
	while curRow < rowCountConstant:
		curRow = curRow+1
		input = fin.readline()
		input = input.strip().split()		
		tempVal = [int(j) for j in input]
		if curRow == firstRowNumber:
			savedInts = tempVal
		
	#Now check that with the 2nd row

	input = fin.readline()
	secondRowNumber = int(input)

	curRow2=0
	while curRow2 < rowCountConstant:
		curRow2 = curRow2 + 1
		input = fin.readline()
		input = input.strip().split()		
		tempVal = [int(j) for j in input]
		if curRow2 == secondRowNumber:
			savedInts2 = tempVal

	#Now it's time to return things!

	z = set(savedInts) & set(savedInts2)

	if len(z) > 1:
		print("Case #%d: Bad magician!" %(i+1))
	elif len(z) < 1: 
		print("Case #%d: Volunteer cheated!" %(i+1))
	else:
		print("Case #%d: %d" %((i+1), next(iter(z))))	
		

