import math

inFile = open("1input.txt")
inFile.readline()
outFile = open("1output.txt", "w")

j = 1

for line in inFile:
    case = line.rstrip().split(" ")[1]
    caseRev = int(case[::-1])
    currSum = 0
    i = 0

    result = 0

    while(caseRev > 0):
        if(currSum < i):
            result += i-currSum
            currSum = i
        
        currSum += caseRev % 10
        caseRev = caseRev // 10

        i += 1

    print("Case #" + str(j) + ": " + str(result), file=outFile)

    j += 1

inFile.close()
outFile.close()
