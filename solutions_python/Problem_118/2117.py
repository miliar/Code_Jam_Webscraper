def isPalindrome(n):
	if int(str(n)[::-1]) == n:
		return True
	else:
		return False

def getInput(prob):
	f = open(prob, "r")
	result = []
	cases = int(f.readline())
	for i in range(cases):
		result.append([int(i) for i in f.readline().replace("\n", "").split(" ")])
	f.close()
	return result

def main(ans, prob):
	inp = getInput(prob)
	
	f = open(ans, "w")
	for i in range(len(inp)):

		f.write("Case #" + str(i + 1) + ": " + str(solveCase(inp[i])) + "\n")
	f.close()

def solveCase(case):

	lowerLim = int(case[0]**(0.5)) 
	higherLim = int(case[1]**(0.5))
	counter = 0
	for i in range(lowerLim, higherLim + 1):
		if isPalindrome(i):
			l = i**2
			if isPalindrome(l) == True and l >= case[0] and l <= case[1]:
				counter+=1
				
	return counter

main("answerSmall.txt", "problemSmall.in")
