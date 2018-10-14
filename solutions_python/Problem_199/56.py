#!python3

inputFile = open("A-large.in", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):
    
    inp = inputFile.readline()
    inp = inp.split()
    
    panCakes = inp[0]
    flipSize = int(inp[1])

    flipQueue = []

    ans = 0

    for index in range(len(panCakes) - flipSize + 1):
        while len(flipQueue) > 0:
            if flipQueue[0] < index:
                flipQueue.pop(0)
            else:
                break

        panSide = panCakes[index]

        if panSide == '+':
            if len(flipQueue) % 2 == 1:
                flipQueue.append(index + flipSize - 1)
                ans = ans + 1
        else:
            if len(flipQueue) % 2 == 0:
                flipQueue.append(index + flipSize - 1)
                ans = ans + 1


    isPossible = True
    for index in range(len(panCakes) - flipSize + 1, len(panCakes)):
        while len(flipQueue) > 0:
            if flipQueue[0] < index:
                flipQueue.pop(0)
            else:
                break

        panSide = panCakes[index]

        if panSide == '+':
            if len(flipQueue) % 2 == 1:
                isPossible = False
        else:
            if len(flipQueue) % 2 == 0:
                isPossible = False

    if isPossible == False:
        ans = "IMPOSSIBLE"

    print("Case #", testCase, ": ", ans, sep="", file=outputFile)

inputFile.close()
outputFile.close()
