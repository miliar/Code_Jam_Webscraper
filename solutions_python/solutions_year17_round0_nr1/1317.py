inputFile =  open("A-large.in",'r')
outputFile = open("output.out",'w')
testCases = int(inputFile.readline())

for testCase in range(1,testCases+1):
    result = 0
    a,b = inputFile.readline().split(" ")
    pancakes = list(a)
    K = int(b)
    index = 0
    while index + K - 1 < pancakes.__len__():
        if pancakes[index] == '-':
            result += 1
            for i in range (0,K):
                if pancakes[index + i] == '-':
                    pancakes[index + i] = '+'
                else:
                    pancakes[index + i] = '-'
        index += 1
    for item in pancakes[pancakes.__len__() - K:]:
        if item == '-':
            result = 'IMPOSSIBLE'
            break
    print("Case #" + str(testCase) + ": " + str(result))
    outputFile.write("Case #"+str(testCase)+": "+str(result)+"\n")
outputFile.close()
