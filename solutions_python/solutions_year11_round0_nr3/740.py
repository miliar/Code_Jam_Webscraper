import sys

def even(l):
    remainder = sum(l)%2
    if remainder == 1:
        return False
    else:
        return True

def leastSigBit(l):
    l = [x%2 for x in l]
    return l

def rightShift(l):
    l = [int(x/2) for x in l]
    return l

def splitCandy(n, c):
    numCandies = int(n)
    candies = map(lambda x: int(x), c.split())
    maxCandy = max(candies)
    while(maxCandy != 0):
        bits = leastSigBit(candies)
        if not even(bits):
            return "NO"
        candies = rightShift(candies)
        maxCandy /= 2
    origCandies = map(lambda x: int(x), c.split())
    return sum(origCandies) - min(origCandies)

filename = sys.argv[1]
f = open(filename, 'r')
testCases = int(f.readline().split()[0])
for i in range(testCases):
    numCandy = f.readline()
    candies  = f.readline()
    result = splitCandy(numCandy, candies)
    print("Case #" + str(i + 1) + ": " + str(result))
f.close()
