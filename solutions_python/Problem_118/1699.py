def makePalindromeLst():
	lst = []
	for i in range(1, 10000001):
		numtoStr = str(i)
		length = len(numtoStr)
		if length % 2 == 0:
			if numtoStr[: length / 2] == numtoStr[length / 2 :][:: -1]:
				lst.append(i)
		else:
			if numtoStr[: length / 2] == numtoStr[length / 2 + 1:][:: -1]:
				lst.append(i)
	return lst

def checkPalindrome(num):
	numtoStr = str(num)
	length = len(numtoStr)
	if length % 2 == 0:
		if numtoStr[: length / 2] == numtoStr[length / 2 :][:: -1]:
			return True
		else:
			return False
	else:
		if numtoStr[: length / 2] == numtoStr[length / 2 + 1:][:: -1]:
			return True
		else:
			return False

palindromeLst = makePalindromeLst()

fairAndSquare = []
for num in palindromeLst:
	squareNum = num ** 2
	if checkPalindrome(squareNum):
		fairAndSquare.append(squareNum)

#f = open('sample.txt', 'r')
#f = open('test.txt', 'r')
f = open ('C-large-1.in', 'r')
#f = open ('B-large.in', 'r')
#f = open('A-large-practice.in', 'r')
f2 = open('output.txt', 'a')

inputNumber = 1
firstFlg = 1
for line in f:
	line = line.split()
	if firstFlg:
		numOfInput = int(line[0])
		firstFlg = 0
	else:
		result = 0
		minNum = int(line[0])    #minNum >= 1
		maxNum = int(line[1])
		for n in fairAndSquare:
			if n >= minNum and n <= maxNum:
				result = result + 1
			elif n > maxNum:
				break

		f2.write('Case #' + str(inputNumber) + ': ' + str(result) + '\n')
		inputNumber = inputNumber + 1

f2.close()
f.close()
	