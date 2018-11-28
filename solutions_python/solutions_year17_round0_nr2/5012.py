def getDigits(number):
	###returns an array with the digits of the number from last to first###
	digits = []
	while(number!=0):
		rem = number%10
		digits.append(rem)
		number = number/10
	return digits

def isTidy(ls):
	###checks if the sorted array is equal to the number array###
	if sorted(ls, reverse = True) == ls:
		return True
	return False

if __name__ == "__main__":

	no_of_cases = input()
	case = []
	for num in range(0, no_of_cases):
		inp = input()
		case.append(inp)
	
	largestPossible = 0
	count = 0
	for integer in case:
		count+=1
		for num in xrange(0, integer+1):
			arr = getDigits(num)
			if(isTidy(arr)):
				largestPossible = num
				
		ans = "Case #"+str(count)+": "+str(largestPossible)
		print ans
	

			

















