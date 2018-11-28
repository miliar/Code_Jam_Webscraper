def getMinFriends():
    fOutput = open('Output.txt', 'w')
    fInput = open('A-large.in')
    testCount = int(fInput.readline())
    test = 0
    for line in fInput:
        N, arr = line.split()
        N = int(N)
        result = 0
        standUp = 0
        for i in xrange(N + 1):
            currCount = int(arr[i])
            if currCount != 0:
                if i <= standUp:
                    standUp += currCount
                else:
                    result += i - standUp
                    standUp += i - standUp + currCount
        fOutput.write("Case #{test}: {result}\n".format(test=test + 1, result=result))
        test += 1
        print test
    fInput.close()
    fOutput.close()


getMinFriends()
