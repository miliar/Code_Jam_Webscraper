
#to check if num is tidy
def isTidy(num):

	numS = str(num)
	
	lengthOfDigit = len(numS)
	
	#checking from left to right if 0 is less than 1
	for i in range(0,lengthOfDigit-1):
		#is left digit is greater than right one number is not tidy
		if (numS[i]>numS[i+1]):
			return 0

	return 1


#getting last number from the list
def processTidy(num):
	while (num>0):
		if(isTidy(num)==1):
			return num
		num-=1
	
	return -1

# print( processTidy(10022) )


#input file
inputFile = open("B-small-attempt1.in","r")

#output file
outputFile = open("out","a+")

#in each line
caseNumber = 1

linum = 1

# writing file

for line in inputFile:
	num = (int(line))
	# print("number is :",num)
	if linum==1:
		TestCase = num
		linum+=1
	else:
		# print(processTidy(num))
		outLine = "Case #{}: {}".format(linum-1,processTidy(num))
		print(outLine)
		outLine+="\n"
		outputFile.write(outLine)
		linum+=1
	