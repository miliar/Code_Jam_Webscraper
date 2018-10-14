def checkTidy(number):
	
	number = str(number)
	for x in range(len(number)-1):
		if int(number[x]) > int(number[x+1]):
			return False
			
	return True

def getAnswer(number):
	
	while (checkTidy(number) == False):
		number -= 1
		
	return number

testCases = int(input())
answers = []

for x in range(testCases):
	number = int(input())
	answers.append(getAnswer(number))
	
for x in range(len(answers)):
	print ("Case #" + str(x+1) + ": " + str(answers[x]))
	
			
