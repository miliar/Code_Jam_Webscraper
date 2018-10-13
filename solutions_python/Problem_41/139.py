import os
import sys
import logging

logger = logging.getLogger('MinimumScalarPrdt')
logger.setLevel(logging.INFO)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


def computeNextNumber(testCase):
	logger.debug(testCase)
	numberList =[]
	for char in testCase:
		numberList.append(int(char))
	#numberList.sort()
	length=len(testCase)-1
	testCaseList =list(testCase)
	unchangeList=[]
	flag=0
	while length>=0:
		digit =int(testCaseList[length])
		logger.debug("digit is %i" %digit)
		x = len(testCase)-1
		while x> length:
			logger.debug('1 '+str(testCaseList[x]))
			logger.debug('2 '+str(testCaseList[length]))
			if int(testCaseList[x]) > int(testCaseList[length]):
				#y = length
				testCaseList[length]=testCaseList[x]
				testCaseList[x]=str(digit)
				testCaseNew= testCaseList[length+1:]
				testCaseNew.sort()
				logger.debug(testCaseNew)
				logger.debug(testCaseList[:length+1])
				testCaseList = testCaseList[:length+1]+testCaseNew
				#while digit > int(testCaseList[y+1]) and y < len(testCase):
				#		y=y+1
				#		logger.debug('3 '+str(testCaseList[y]))
				#testCaseList[x]=testCaseList[y+1]
				#testCaseList[y+1]=digit
				flag=1
				break
			x-=1
		if flag:
			break
		length-=1
	if not flag:
		testCaseList.insert(1, 0)
		count=0
		testCaseList.sort()
		while count< len(testCaseList):
			if(int(testCaseList[count])!=0):
				temp = testCaseList[0]
				testCaseList[0]=testCaseList[count]
				testCaseList[count]=temp
				break
			count+=1
		testCaseNew=testCaseList[2:]
		testCaseNew.sort()
		testCaseList= testCaseList[0:2]+testCaseNew
		
		
		
	return "".join(str(x) for x in testCaseList)

def solve(input , output):
	numberOfTestCases = int(input.readline().strip())
	for i in range(numberOfTestCases):
		testCase = input.readline().strip()
		nextNumber = computeNextNumber(testCase)
		output.write('Case #%i: %s\n' %(i+1, nextNumber))
		

def main():
	input = open(sys.argv[1], 'r')
	output = open(sys.argv[2], 'w')
	solve(input, output)
	input.close()
	output.close()



if __name__=='__main__':
	main()
