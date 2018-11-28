import math

def isPalindrome(inString):
    isValid = True
    for index in range(math.ceil(len(inString)/2.0)):
        if inString[index] is not inString[-(index + 1)]:
            isValid = False
            break
    return isValid

def isFairSquare(num):
    root = math.sqrt(num)
    return (root.is_integer() and isPalindrome(str(int(root))))

def isFairAndSquare(num):
    isValid = isFairSquare(num)
    return (isValid and isPalindrome(str(num)))

numcases = int(input())

for x in range(0, numcases):
    line = input()
    splitline = line.strip().split()
    start = int(splitline[0])
    end = int(splitline[1])
    counter = 0
    for number in range(start, end + 1):
        if isFairAndSquare(number):
            #print(number)
            counter += 1
    print("Case #{casenum}: {fsnum}".format(casenum = x + 1, fsnum = counter))
