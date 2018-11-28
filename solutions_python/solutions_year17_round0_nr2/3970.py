#! /usr/bin/env python

def popDigit(n):
	#print("Popping a digit from: ", n, " :: ", n//10, n%10)
	return n//10, n%10
#.......................................

def getDigits(n):
	# Boundary case
	if n == 0:
		return [0] 
	# Main calculation
	digits = []
	while n > 0:
		n, digit = popDigit(n)
		digits.append(digit)
	
	#print("Parsed digits: ", digits)
	return digits[::-1] # Reversed
#.......................................

def resetTailDigits(p, digits):
	return(
		[9 if i >= p else digits[i] 
			for i in range(len(digits))
		]
	)


def tidyDigits(digits):
	#print("Initial digits: ", digits)
	for i in range(len(digits)-1):
		
		if digits[i+1] < digits[i]:
			digits[i] -= 1
			digits = resetTailDigits(i+1, digits)
			#print("Checking again: ", digits)
			return tidyDigits(digits)
		
	return digits
#.......................................

def digitsToInteger(digits):
	#print("Final digits: ", digits)
	rev_digits = digits[::-1]
	return( 
		sum(
			[rev_digits[i]*(10**i) 
				for i in range(len(rev_digits))
			]
		)
	)
#.......................................

def tidyNumber(n):
	return( 
		digitsToInteger(
			tidyDigits(
				getDigits(n)
			)
		)
	)
#.......................................


#===========>MAIN FUNCTION<================

if __name__ == "__main__":
	
	# Initialize
	from collections import deque
	n_cases = int( input() )
	cases = []
	
	# Read cases
	for i in range(n_cases):
		cases.append( int( input() ) )
	
	# Print cases
	cases = deque(cases)
	for i in range(n_cases):
		print("Case #%d: " % (i+1), tidyNumber( cases.popleft() ))