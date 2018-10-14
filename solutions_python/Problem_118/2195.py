import math

def isPalendrome(x):
    strX = str(x)
    return strX[:len(strX)/2] == strX[:(len(strX) - 1)/2:-1]

cases = int(raw_input())

for case in range(cases):
    bounds = [int(x) for x in raw_input().split(' ')]
    lowerChildBound = int(math.ceil(math.sqrt(bounds[0])))
    upperChildBound = int(math.floor(math.sqrt(bounds[1])))

    numPalendromes = 0
    for i in range(lowerChildBound, upperChildBound + 1):
        if isPalendrome(i):
            if isPalendrome(i**2):
                numPalendromes += 1

    print "Case #" + str(case + 1) + ": " + str(numPalendromes)

