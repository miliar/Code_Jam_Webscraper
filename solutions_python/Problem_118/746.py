
import string, os, time, sys, math
"""
# Count # instances of value on the lawn
def LawnCount(lawn, M, N, value):
    lawnCount = 0
    for i in range(0,M):
        lawnCount += lawn[i].count(value)
    return lawnCount

# Replace all instances of value on lawn with newValue
def ReplaceOnLawn(lawn, M, N, value, newValue):
    for i in range(0,M):
        for j in range(0,N):
            if (lawn[i][j] == value):
                lawn[i][j] = newValue

# Can the entire row be unmowed (i.e. is it all the current value)?
def CanUnmowRow(lawn, row, N, value):
    for i in range(0,N):
        if (abs(lawn[row][i]) != value):
            return False;
    return True

# Unmow the row (set its value to negative).
def UnmowRow(lawn, row, N, value):
    for i in range(0,N):
        lawn[row][i] = value * -1
    
# Can the entire column be unmowed (i.e. is it all the current value)?
def CanUnmowCol(lawn, M, col, value):
    for i in range(0,M):
        if (abs(lawn[i][col]) != value):
            return False;
    return True

# Unmow the column (set its value to negative).
def UnmowCol(lawn, M, col, value):
    for i in range(0,M):
        lawn[i][col] = value * -1
"""


def IsPalindrome(n):
    if (n%10 == 0):
        return False
    lastDigit = 0
    reverse = 0
    while (n > reverse):
        lastDigit = n%10
        reverse=reverse*10+lastDigit
        n = n/10
    if n == reverse:
        return True
    n = n*10+lastDigit
    return n == reverse

def NumDigits(n):
    if (n<1e6):
        if (n<1e3):
            if     n<10: return 1
            elif  n<100: return 2
            else:        return 3
        else:
            if    n<1e4: return 4
            elif  n<1e5: return 5
            else:        return 6
    else:
        if n<1e10:
            if    n<1e8:
                if n<1e7: return 7
                else:     return 8
            else:
                if n<1e9: return 9
                else:      return 10
        else:
            if n<1e12:
                if n<1e11: return 11
                else:      return 12
            else:
                if n<1e13:    return 13
                elif n<1e14:  return 14
                else:         return 15

def NextPalindrome(n):
    numDigits = NumDigits(n)
    if n == 10**numDigits-1:
        return n+2
    numMirroredDigits = numDigits/2
    truncateFactor = (10**numMirroredDigits)
    firstHalf = n / truncateFactor
    firstHalf += 1
    result = firstHalf*truncateFactor
    partToReverse = firstHalf
    if numDigits % 2 != 0:
        partToReverse /= 10
    reverse = 0
    while partToReverse > 0:
        lastDigit = partToReverse%10
        reverse = reverse*10 + lastDigit
        partToReverse /= 10
    return result + reverse
        

def FirstPalindromeAfter(n, squareAtLeast):
    result = -1
    while result < n or result*result<squareAtLeast:
        result = NextPalindrome(result)
    return result


def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n")
    splitline = caseline.split(" ")
    A = int(splitline[0])
    B = int(splitline[1])

    found = 0
    start = int(math.sqrt(A))
    if not IsPalindrome(start) or start*start<A:
        start = FirstPalindromeAfter(1, A)

    current = start
    square = current*current
    while square <= B:
        if IsPalindrome(square):
            found += 1
        current = NextPalindrome(current)
        square = current*current

    print "Case #%(count)d: %(found)d" % {"count":caseIndex, "found":found}



inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

