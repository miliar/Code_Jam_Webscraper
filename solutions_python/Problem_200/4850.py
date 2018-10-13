for case in range(int(input())):
	def checkIfTidy(number):
		for j in range(len(number)-1):
			if number[j] > number[j+1]:
				return False
		return True
	def testNumber(numberToCheck):
		for i in range(int(numberToCheck),0,-1):
			i = str(i)
			if checkIfTidy(i):
				return(i)
	numberToCheck = str(input())
	print("Case #" + str(case+1) + ": " + str(testNumber(numberToCheck)))