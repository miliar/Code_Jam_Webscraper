import numpy as np
import sys

def isPalindrome(digits):
    length = np.size(digits)
    if length == 1: return True
    half = digits[:length / 2][::-1]
    addition = length % 2
    return np.size(np.where(digits[(length / 2) + addition:] != half)) == 0

data = [line.strip() for line in file(sys.argv[1])]
cases = int(data[0])

for case in range(1, cases + 1):
    A, B = map(int, data[case].split(" "))

    increment = 0
    numberOfFairsAndSquares = 0
    for i in range(A, B + 1):
        number = i
        digits = np.array(list(str(number)))
        if isPalindrome(digits):
            # Take the square root.
            squareroot = np.sqrt(number)
            if squareroot == int(squareroot):
                sqdigits = np.array(list(str(int(squareroot))))
                if isPalindrome(sqdigits):
                    numberOfFairsAndSquares += 1

        increment = np.power(10, np.size(digits) - 2) - 1
        if increment < 1:
            increment = 0
        i += increment
    print 'Case #%s: %s' % (case, numberOfFairsAndSquares)
