import sys
from math import sqrt
 
infile = sys.stdin

def checkNumber(number):
    fromFront = str(number)
    if int(number) == number:
        fromFront = str(int(number))
    fromEnd = fromFront[::-1]
    return fromFront == fromEnd

def fairAndSquare(start, end):
    foundNumbers = 0
    for i in range(start, end+1):
        fair = checkNumber(i)
        square = checkNumber(sqrt(i))
        if fair and square:
            foundNumbers = foundNumbers + 1
    return foundNumbers

T = int(infile.readline())
for i in xrange(T):
    tokens = infile.readline().split()
    result = fairAndSquare(int(tokens[0]), int(tokens[1]))
    print("Case #%d: %s" % (i+1, result))
