import numpy
import re

t = int(input()) # Number of test cases
for i in range(t):
    s = input() # Given test case string
    lenNumber = len(s)
    tidyNumber = s
    # tidyNumber = s if lenNumber = 1
    if lenNumber > 1:
        numStrList = list(s)
        # initialize number
        number = numpy.zeros((lenNumber))
        decreasingIndex = -1
        for j in range(lenNumber):
            number[j] = numStrList[j]
            # Find the index at which order is decreasing
            if j > 0:
                if number[j - 1] > number[j] \
                    and decreasingIndex == -1:
                        decreasingIndex = j

        # Proceed if order is decreasing
        if decreasingIndex != -1:
            # Compare against num with same # of digits, all same as 1st
            sameDigits = numpy.full((lenNumber), number[0])
            originalNum = int(''.join(re.sub('\.0', '', str(num)) for num in number))
            sameDigitNum = int(''.join(re.sub('\.0', '', str(num)) for num in sameDigits))

            if originalNum > sameDigitNum:
                # Decrease digit previous to the one at decreasingIndex
                number[decreasingIndex - 1] = number[decreasingIndex - 1] - 1
                # Fill 9s starting at decreasingIndex
                number[decreasingIndex:] = 9
            else:
                # Decrease 1st digit
                number[0] = number[0] - 1
                # Fill 9s starting at 1st index
                number[1:] = 9

            tidyNumber = ''.join(re.sub('\.0', '', str(num)) for num in number)
            tidyNumber = re.sub('^0', '', tidyNumber)

    print("Case #{}: {}".format(i + 1, tidyNumber))
