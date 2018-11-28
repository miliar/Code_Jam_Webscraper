def inputCases(fileName):
	f = open(fileName, 'r')
	numberOfTestCases = int(f.readline())
	TestCases = []
	for i in range(0,numberOfTestCases):
		TestCase = int(f.readline())
		TestCases.append(TestCase)
	f.close()
	return TestCases
def saveResult(fileName, data):
	f = open(fileName, 'w')
	j = 1
	for i in data:
		f.write("Case #" + str(j) + ": " + str(i) + "\n")
		j+=1
	f.close()
	return TestCases

def Increasing(number):
	digits = list(str(number))
	for i in range(1, len(digits)):
		if (int(digits[i]) < int(digits[i-1])):
			return False;
	return True;
def ZerosAndOnes(number):
	digits = list(str(number))
	for i in range(0, len(digits)):
		if (digits[i] != '0' and digits[i] != '1'):
			return False;
	return True;
def Tildy(number):
	if (number < 10):
		return True;
	elif(Increasing(number)):
		return True;
	else:
		return False;
def MakeTildy(number):
	if (ZerosAndOnes(number)):
		return int('9' * (len(str(number))-1))
	else:
		number-=1
	if(Tildy(number)):
		return number
	else:
		return MakeTildy(number)
TestCases = inputCases('input.txt')
Results = []
for i in TestCases:
	if (Tildy(i)):
		Results.append(i)
	else:
		Results.append(MakeTildy(i))
saveResult('output.txt', Results)