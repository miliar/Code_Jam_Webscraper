import sys, gmpy2, math
# gmpy2 contains multiple-precision arithmetic for Python.
# It can be downloaded here:
# https://code.google.com/p/gmpy/downloads/detail?name=gmpy2-2.0.0.win-amd64-py3.3.exe&can=2&q=

fileIn = open('C-small-attempt1.in', 'r')
fileOut = open('output.txt', 'w+')

testCases = int(fileIn.readline())

# Check if number is palindromic
def isPalindrome(test):
    if str(test) == str(test)[::-1]:
        return True
    else:
        return False

# Check if number is perfect square.
# USES EXTERNAL ARITHMETIC LIBRARY: gmpy2 - link provided at top
def isSquare(test):
    return gmpy2.is_square(test) and isPalindrome(int(math.sqrt(value)))
    

for case in range(0, testCases):
    interval = list(map(int, fileIn.readline().strip().split(' ')))
    count = 0

    for value in range(interval[0], interval[1] + 1):
        if isPalindrome(value) and isSquare(value):
            count += 1

    fileOut.write('Case #'
                  + str(case + 1)
                  + ': '
                  + str(count)
                  + '\n')

fileIn.close()
fileOut.close()
            
