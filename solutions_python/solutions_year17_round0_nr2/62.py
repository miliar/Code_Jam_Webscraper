#!python3

inputFile = open("B-large.in", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    inp = int(inputFile.readline())

    num = []

    inp1 = inp
    while inp1 > 0:
        num.insert(0, inp1 % 10)
        inp1 = inp1 // 10

    isNotCorrect = True

    while isNotCorrect:
        isNotCorrect = False
        
        index = -1
        for i in range(1, len(num)):
            if num[i - 1] > num[i]:
                index = i - 1
                isNotCorrect = True
                break

        if index >= 0:
            num[index] = num[index] - 1

            for i in range(index + 1, len(num)):
                num[i] = 9

    ans = 0
    for i in range(len(num)):
        ans = (ans * 10) + num[i]
    
    print("Case #", testCase, ": ", ans, sep="", file=outputFile)

inputFile.close()
outputFile.close()
