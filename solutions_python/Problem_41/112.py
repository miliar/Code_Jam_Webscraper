import sys
cachedBaseFails = {}

def numToListForm(num):
	while num > 0:
		digit = num % 10
		num = num / 10
		listForm = listForm + [digit]
	return listForm

def listFormToNum(listForm):
	num = 0
	listForm.reverse()
	for digit in listForm:
		num = num * 10 + digit
	return num

if __name__ == "__main__":
	lines = sys.stdin.read().split("\n")
	
	numText = int(lines[0])
	
	caseNum = 0
	for line in lines[1:]:
		if caseNum >= numText:
			break
		caseNum += 1
		
		test = int(line)
		
		numCounts = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
		numLessThan = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
		listForm = []
		numDigits = 0
		smallestDigit = 10
		largestDigit = 0
		numNonZero = 0
		
		tempNum = test
		while tempNum > 0:
			numDigits += 1
			digit = tempNum % 10
			if digit < smallestDigit:
				smallestDigit = digit
			if digit > largestDigit:
				largestDigit = digit
			if digit > 0:
				numNonZero += 1
			listForm = listForm + [digit]
			numCounts[digit] += 1
			tempNum = tempNum / 10
		
		if numNonZero == 1:
			num = test * 10
			outputStr = "Case #" + str(caseNum) + ": " + str(num)
			print outputStr
			continue
		
		counter = 0
		for i in range(1,10):
			counter += numCounts[i-1]
			numLessThan[i] = counter
		
		#print listForm
		#print smallestDigit, largestDigit
		#print numLessThan
		
		swapIndex = -1
		swapNumber = 0
		lessThanCounter = 0
		swapped = False
		wantToSwap = {}
		for i in range(0,numDigits):
			digit = listForm[i]
			if swapIndex == -1:
				if numLessThan[digit] > lessThanCounter:
					swapIndex = i
					swapNumber = digit
					wantToSwap[swapNumber] = swapIndex
				else:
					lessThanCounter += 1
			elif swapNumber > digit:
				for j in range(digit+1, 10):
					if j in wantToSwap:
						swapNumber = j
						swapIndex = wantToSwap[j]
						listForm[swapIndex] = digit
						listForm[i] = swapNumber
						flipPart = listForm[0:i]
						flipPart.reverse()
						listForm = flipPart + listForm[i:]
						swapped = True
						break
				if swapped == True:
					break
			elif digit > swapNumber:
				swapIndex = i
				swapNumber = digit
				wantToSwap[swapNumber] = swapIndex
				
				
		
		if swapped == True:
			outputStr = "Case #" + str(caseNum) + ": " + str(listFormToNum(listForm))
		else:
			if listForm[0] == 0:
				for i in range(1,numDigits):
					digit = listForm[i]
					if digit > 0:
						listForm[0] = digit
						listForm[i] = 0
						break
				
			listForm.reverse()
			listForm = listForm[0:-1] + [0] + listForm[-1:]
			outputStr = "Case #" + str(caseNum) + ": " + str(listFormToNum(listForm))
		print outputStr