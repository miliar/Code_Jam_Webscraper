def getSecsCount():
    fOutput = open('Output.txt', 'w')
    fInput = open('B-large.in')
    testCount = int(fInput.readline())
    for test in xrange(testCount):
        D = int(fInput.readline())
        dinners = map(int, fInput.readline().split())
        result = max(dinners)
        maxi = max(dinners)
        for wantDinner in xrange(1, maxi):
            seconds = 0
            for dinner in dinners:
                if dinner > wantDinner:
                    seconds += dinner / wantDinner - 1 if dinner % wantDinner == 0 else dinner / wantDinner
                if seconds + wantDinner >= result:
                    break
            if seconds + wantDinner < result:
                result = seconds + wantDinner
        fOutput.write("Case #{test}: {result}\n".format(test=test + 1, result=result))
    fInput.close()
    fOutput.close()

getSecsCount()
