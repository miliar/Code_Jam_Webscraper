#!python3

inputFile = open("C-large.in", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    inp = inputFile.readline().split()

    n = int(inp[0])
    k = int(inp[1])

    baseCount = 1
    while k > baseCount:
        k -= baseCount
        baseCount *= 2

    stallLen = (n - k + 1) // baseCount

    minLen = (stallLen - 1) // 2
    maxLen = stallLen // 2
    
    print("Case #", testCase, ": ", maxLen, " ", minLen, sep="", file=outputFile)

inputFile.close()
outputFile.close()
