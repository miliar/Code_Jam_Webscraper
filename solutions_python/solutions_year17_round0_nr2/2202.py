
"""

Basic idea:
	Find the longest non-decreasing sequence of digits that starts that the beginning of the number.
	If this sequence is the whole number, then the input was tidy, so output it
	Otherwise, we find the last digit in the non-decreasing sequence, except that if that digit is repeated in the non-decreasing sequence,
		we walk backwards until we find the first time that digit occurred in the non-decreasing sequence.  We then decrease the digit we found
		by one, and set all digits after it to a 9, forming the smallest tidy number smaller than the input.
	If the digit we were set to decrease was the leading digit and was a 1, we need to make sure we don't include a leading zero

"""

def getNumDigits(num):
	"""Get the number of digits in an integer num.
		I know that this can be done more easily using a log base 10, but Python's built in log function
		has numerical precision issues and was saying that the log of 1000 was just slightly less than 3,
		and I'm concerned that it would also fail in other cases."""
	numDigits = 0
	while num > 0:
		num = num // 10
		numDigits += 1
	return numDigits

def getDigit(num, pos):
	"""Given an integer num, returns the digit at position pos, where position 0 is the ones place
		If num has fewer digits than pos, raises a ValueError"""
	numDigits = getNumDigits(num)
	if pos >= numDigits:
		raise ValueError("Asked for digit in position " + str(pos) + ", but " + str(num) + " only has " + str(numDigits) + " digits!")
	ret = num // (10**pos) # trim off lower digits
	return ret % 10 # return the digit that is now in the ones place

def getLastTidyDigit(num):
	"""Given an integer num, returns the position of the last "tidy" digit:
		the last digit for which the previous digits formed a non-decreasing sequence"""
	lastPos = getNumDigits(num) - 1 # the right-most position in the number --> number of digits minus 1 for zero-indexing
	currPos = lastPos - 1 # the leading digit is guaranteed to be tidy, so start checking from the second-to-left
	prevDigit = getDigit(num, lastPos)
	while currPos >= 0:
		currDigit = getDigit(num, currPos)
		if currDigit < prevDigit:
			return currPos + 1 # this digit isn't tidy, but the last one was
		prevDigit = currDigit
		currPos -= 1
	# if got to here, the whole number is tidy, so the last tidy digit is the one to the far right
	return 0

numInputs = int(input())

for case in range(1, numInputs + 1):
	lastNum = int(input())
	lastTidyDigit = getLastTidyDigit(lastNum)
	if lastTidyDigit == 0:
		# means that the whole number is tidy, so just output it
		print("Case #" + str(case) + ": " + str(lastNum))
		continue # move on to the next number

	# otherwise, walk backwards from the last tidy digit to find the first time it appeared in the non-decreasing sequence
	numDigits = getNumDigits(lastNum)
	firstAppearence = lastTidyDigit
	compareDigit = getDigit(lastNum, firstAppearence)
	while firstAppearence < numDigits - 1:
		currDigit = getDigit(lastNum, firstAppearence + 1)
		if currDigit == compareDigit:
			firstAppearence += 1
		else:
			break
	# if all the digits out to the beginning of the number are the same, firstAppearence will go up to numDigits - 1 (the leading digit),
	#	then exit the loop, so we still get the right answer

	if firstAppearence ==  numDigits - 1:
		# number we're decreasing by one was the leading digit -- it's easier to treat this separately
		out  = ""
		if compareDigit != 1:
			# make sure we don't accidentally include a leading zero
			out = str(compareDigit - 1)
		out += "9" * (numDigits - 1)
		print("Case #" + str(case) + ": " + out)
		continue # move on to the next number

	leadingDigits = lastNum // (10 ** (firstAppearence + 1)) # the digits to the left of firstAppearence don't change
	out = str(leadingDigits) + str(compareDigit - 1) # we're guaranteed that compareDigit != 0, since 0 is the smallest digit and so can't be at the end of a non-decreasing sequence
	out += "9" * firstAppearence # all the digits to the right of firstAppearence become 9
	print("Case #" + str(case) + ": " + out)