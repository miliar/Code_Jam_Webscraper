
def checkIfPalindrome(number):
	fnord = str(number)
	for x in range(len(fnord)):
		if(fnord[x]!=fnord[-x-1]):
			return False
	return True

def getPalindromesInRange(a,b):
	result=[]
	for x in range(a,b+1):
		if(checkIfPalindrome(x)):
			result.append(x)
	return result
	
def getSquareAndFairInRange(a,b):
	palindromes = getPalindromesInRange(a,b)
	result = 0
	i = -1
	while(True):
		i+=1
		square = i*i
		if(square>b):
			break
		if((a <= square <= b) & (square in palindromes) & (checkIfPalindrome(i))):
			result += 1
	return result
	

input = open('c:\\users\\snuff\\desktop\\codeJam\\C-small-attempt0.in','r+')
output = open('c:\\users\\snuff\\desktop\\codeJam\\c-small.out','w+')

case = 0
input.readline()
for line in input:
	case+=1
	a,b = line.split()
	print("Case #%i: %i"%(case,getSquareAndFairInRange(int(a), int(b))), file=output)
