import linecache
import shlex

#name of file with testing data
inputFile = 'B-large.in'

#number of test cases
totalTestCases = int(linecache.getline(inputFile, 1))


for i in xrange(2, totalTestCases + 2):
    timeSpent = float(0)
    cookieProduction = 2.0
    inputData = (shlex.split(linecache.getline(inputFile, i)))
    factoryCost = float(inputData[0])
    factoryDelta = float(inputData[1])
    targetCookies = float(inputData[2])
    waitForTarget = targetCookies / cookieProduction
    waitForFactoryAndTarget = (factoryCost / cookieProduction) + (targetCookies / (cookieProduction + factoryDelta))
    if waitForTarget > waitForFactoryAndTarget:
        while waitForTarget > waitForFactoryAndTarget:
            timeSpent += (factoryCost / cookieProduction)
            cookieProduction += factoryDelta
            waitForTarget = targetCookies / cookieProduction
            waitForFactoryAndTarget = (factoryCost / cookieProduction) + (targetCookies / (cookieProduction + factoryDelta))
        print "Case #%d: %s " % (i-1, "{0:.7f}".format(timeSpent + waitForTarget))
    else:
        print "Case #%d: %s " % (i-1, "{0:.7f}".format(waitForTarget))

