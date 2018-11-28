import sys

count = 0
for line in sys.stdin:
	if count == 0:
		num_tests = int(line)
		count += 1
	else:
		number = int(line)
		count += 1
		numberList = [int(d) for d in str(number)]
		if sorted(numberList) == numberList:
			print "Case #" + str(count-1) + ": " + str(number)
		else:
			highestNumber = 0
			index = 0
			while 1 > index:
				try:
					highestNumber = numberList[index]
					if numberList[index+1] > highestNumber:
						highestNumber = numberList[index+1]
					else:
						highestNumber = numberList[index]
						pass
				except IndexError:
					pass
				index += 1
			# print highestNumber
			outputList = numberList
			# print "Index of highest number:" + str(outputList.index(highestNumber))
			index = outputList.index(highestNumber)
			outputList[index] -= 1
			while index < len(outputList):
				try:
					outputList[index+1] = 9
				except IndexError:
					pass
				index += 1
			if outputList[0] == 0:
				outputList.pop(0)
			# print outputList
			outputValue = ""
			for digit in outputList:
				outputValue += str(digit)
			print "Case #" + str(count-1) + ": " + str(outputValue)
