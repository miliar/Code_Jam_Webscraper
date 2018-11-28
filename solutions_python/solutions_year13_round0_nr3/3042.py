import math
def isFairSquare(num):		
	if isSquare(num):
		return (isFair(int(num)) and isFair(int(math.sqrt(num))))
	else:
		return False
	
def isSquare(num):
	return (math.sqrt(num)%1==0)
	

	
def isFair(num):
	num=str(num)
	revnum=""
	for i in range(len(num)):
		revnum=num[i]+revnum
	revnum=int(revnum)
	num=int(num)
	if (num==revnum):	
		return True
	else:
		return False
	
def getFairSquareCount(startRange,endRange):	
	count=0
	for i in range(startRange,endRange+1):
		if(isFairSquare(i)):
			count+=1
	return count

def  main():
	input=open("C-small-attempt1.in","r+")
	output=open("fair.txt","w")
	testCase=int(input.readline())
	caseCount=1	
	for i in input:
		i=i.split(" ")
		startRange=int(i[0])
		endRange=int(i[1])
		fairSquareCount=getFairSquareCount(startRange,endRange)
		output.write("Case #{1}: {0}\n".format(fairSquareCount,caseCount))
		caseCount+=1	
	input.close()
	output.close()
main()	