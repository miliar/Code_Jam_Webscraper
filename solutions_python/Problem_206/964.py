inputFile =  open("A.in",'r')
outputFile = open("output.out",'w')
testCases = int(inputFile.readline())

for testCase in range(1,testCases+1):
    result = 0
    a,b = inputFile.readline().split(" ")
    D = int(a)
    N = int(b)
    maxTime = 0
    for i in range(N):
        x,y = inputFile.readline().split(" ")
        K = int(x)
        S = int(y)
        time = (D-K)/S
        if (time>maxTime):
            maxTime = time
        result = D/maxTime
    print("Case #" + str(testCase) + ": " + str(result))
    outputFile.write("Case #"+str(testCase)+": "+str(result)+"\n")
outputFile.close()
