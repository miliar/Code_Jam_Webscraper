def findLargestNonDecreasingPrefixLen(num):
    numStr = str(num)

    for i in range(1, len(numStr)):
        if(int(numStr[i]) < int(numStr[i-1])):
            return i

    return len(numStr)

def doNum(num):
    prefixLen = findLargestNonDecreasingPrefixLen(num)
    prefix = str(num)[:prefixLen]
    if(prefixLen < len(str(num))):
        prefixNum = int(prefix)-1
        return int(str(doNum(prefixNum)) + "9"*(len(str(num))-prefixLen))

    return int(prefix)

def doNaive(num):
    while(True):
        if(findLargestNonDecreasingPrefixLen(num) == len(str(num))):
            return num
        num -= 1

inFile = open("B-large.in")
outFile = open("B-large.out", "w")

cnt = int(inFile.readline().rstrip())

for i in range(1, cnt+1):
    num = int(inFile.readline().rstrip())
    result = doNum(num)
    print("Case #" + str(i) + ": " + str(result), file=outFile)

outFile.close()
