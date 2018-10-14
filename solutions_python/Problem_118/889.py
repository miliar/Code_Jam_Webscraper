import math

def get_half(fullDigits): # starting half
    lengthDigits = int(math.log10(fullDigits))
    return fullDigits // (10 ** ((lengthDigits + 1) // 2))

def get_half2(fullDigits): # endings half backwards
    lengthDigits = int(math.log10(fullDigits))
    result = 0
    for power in range(lengthDigits // 2 + 1):
        result += (fullDigits % (10 ** (power + 1))) // (10 ** power) * (10 ** (lengthDigits // 2 - power))
    return result

def get_full(halfDigits, isEven = True):
    lengthDigits = int(math.log10(halfDigits))
    fullDigits = halfDigits * (10 ** (lengthDigits + isEven))
    for power in range(1 * (not isEven), lengthDigits + 1):
        fullDigits += ((halfDigits % (10 ** (power + 1))) // (10 ** power)) * (10 ** (lengthDigits - power))
    return fullDigits

def next_half(half, isEven): # return next half, and if to change isEven
    nextHalf = half + 1
    if int(math.log10(nextHalf)) > int(math.log10(half)):
        if isEven:
            return nextHalf, True
        else:
            return nextHalf / 10, True
    else:
        return nextHalf, False


fair = [1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004]

inputFile = open("C-large-1.in", "r")
#inputFile = open("QualificationCsmall.in", "r")
outputFile = open("QualificationCsmall.txt", "w")

cases = int(inputFile.readline().strip())

for caseIndex in range(1, cases + 1):
    lowerLimit, upperLimit = map(int, inputFile.readline().strip().split(" "))
    fairNumbers = 0
    for item in fair:
        if item > upperLimit:
            break
        if item >= lowerLimit:
            fairNumbers += 1
##    lowerSqrt = int(math.ceil(math.sqrt(lowerLimit)))
##    upperSqrt = int(math.sqrt(upperLimit))
##
##    startEven = int(math.log10(lowerSqrt)) % 2
##    half = get_half(lowerSqrt)
##    if lowerSqrt > get_full(half, startEven):
##        half += 1
##    even = startEven
##    fairNumbers = 0
##
##    while True:
##        full = get_full(half, even)
##        if full > upperSqrt:
##            break
##        square = full ** 2
##        if get_half(square) == get_half2(square):
##            fairNumbers += 1
##            print square
##        nextHalf = next_half(half, even)
##        if nextHalf[1] == True:
##            even = not even
##        half = nextHalf[0]

    #outputFile.write("%d %d\n" % (lowerLimit, upperLimit))
    outputFile.write("Case #%d: %d\n" % (caseIndex, fairNumbers))



inputFile.close()
outputFile.close()