inputFile = "inputB.txt"
outputFile = "outputB.txt"

f = open(inputFile, "r")
f.readline()
wf = open(outputFile, "w")


def findTidy(num):
    numList = [int(i) for i in str(num)]
    for index in range(len(numList) - 1, 0, -1 ):
        if numList[index] < numList[index - 1]:
                numList[index - 1] = numList[index - 1] - 1
                for i in range(index, len(numList)):
                    numList[i] = 9
    number = map(str, numList)
    number = "".join(number)
    return int(number)


testCase = 1
for line in f:
    n = int(line)
    wf.write("Case #" + str(testCase) + ": " + str(findTidy(n)) + "\n")
    testCase += 1

f.close()
wf.close()