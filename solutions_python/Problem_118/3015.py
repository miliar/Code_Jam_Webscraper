import math
def isNumberPalindrome(number):
        stringNumber = str(number)
        if len(stringNumber) == 1:
            return True
        for i in range(len(stringNumber)/2):
            if stringNumber[i] != stringNumber[-i-1]:
                return False
            return True
def fairAndSquare(min, max):
    result = 0
    for i in range(min, max+1):
        if isNumberPalindrome(i):
            if math.sqrt(i)%1 == 0.0 and isNumberPalindrome(int(math.sqrt(i))):
                result +=1
    return result
def fileIO(filename):
    input = open(filename)
    output = open('output.txt', 'w+')
    testCases = int(input.readline())
    for i in range(testCases):
        line = input.readline()
        borders = line.split()
        output.write('Case #{0}: {1}\n'.format(i+1, fairAndSquare(int(borders[0]), int(borders[1]))))


