import math

inputFile = open("C-small-attempt0.in")

line = inputFile.readline()[:-1]
number = int(line)

def fairAndSquare(number):
    if not isPalindrome(number):
        return False
    if not isPerfectSquare(number):
        return False
    if not isPalindrome(int(math.sqrt(number))):
        return False
    return True

def isPalindrome(number):
    strNumber = str(number)
    strDigs = len(strNumber)
    if strDigs == 1:
        return True
    index = 0
    while index < strDigs:
        if strNumber[index] != strNumber[strDigs - 1 - index]:
            return False
        index += 1
    return True

def isPerfectSquare(number):
    thisSQRT = math.sqrt(number)
    strNumber = str(thisSQRT)
    strDecimal = strNumber[strNumber.index(".") + 1:]
    if len(strDecimal) > 1:
        return False
    if strDecimal[0] == "0":
        return True
    return False

for case in range(number):
    line = inputFile.readline()[:-1]
    endpoints = line.split(" ")
    start = int(endpoints[0])
    end = int(endpoints[1])
    numFNS = 0
    while start <= end:
        if fairAndSquare(start):
            numFNS += 1
        start += 1
    print "Case #" + str(case + 1) + ": " + str(numFNS)
