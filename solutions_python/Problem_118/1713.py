import math

f = open('C-small-attempt0.in')
g = open('C-small-attempt0.txt', 'w')
numCases = f.readline()

def isPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

def isSquare(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def checkFairSquare(number):
    if isPalindrome(number) and isSquare(number):
        return isPalindrome(int(number ** .5))
    return False

for i in xrange(int(numCases)):
    numFairSquare = 0
    a = f.readline()
    a = a.split()
    for b in xrange(int(a[0]), int(a[1]) + 1):
        if checkFairSquare(b):
            numFairSquare += 1
    g.write('Case #{}: {}\n'.format(i + 1, numFairSquare))

f.close()
g.close()
