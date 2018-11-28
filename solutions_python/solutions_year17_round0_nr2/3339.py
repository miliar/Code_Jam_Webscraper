def tidyNumber(number):
	numberList = map(int,str(number))
	digitL = len(numberList)
	if (digitL == 1):
		return number
	# first pass
	increase = True
	minimumD = 0
	prevDigit = numberList[0]
	firstTurningPoint = -1
	for i in xrange(digitL):

		if (numberList[i] < prevDigit):
			increase = False
			if (firstTurningPoint < 0):
				firstTurningPoint = i-1
			
			if (minimumD < numberList[i]):
				minimumD = numberList[i]
				
		prevDigit = numberList[i]
	if (increase):
		return number
	# if there is bumpy point, return the 
	'''
	if (minimumD == 0 and ):
		result = pow(10,digitL-1) - 1
	'''	
	# deal with the case that the turnig point has many same answer
	while (firstTurningPoint >0):
		if (numberList[firstTurningPoint-1] == numberList[firstTurningPoint]):
			firstTurningPoint = firstTurningPoint-1
		else:
			break
	result = (number/pow(10,digitL-firstTurningPoint-1))*pow(10,digitL-firstTurningPoint-1) -1	
	return result	


T = int(raw_input())
for i in xrange(T):
	N = int(raw_input())
	result = tidyNumber(N)
	print('Case #{}: {}'.format(i+1, result))




	
				















