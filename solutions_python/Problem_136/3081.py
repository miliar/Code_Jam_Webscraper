import sys

def readRowAsInt(filehandle):
    return int(filehandle.readline())

def readRowAsFloats(filehandle):
    line = filehandle.readline()
    return [ float(v) for v in line.split(" ") ]

def main():
    filehandle = open(sys.argv[1], 'r')
    numTestCases = readRowAsInt(filehandle)

    for caseNumber in xrange(1, numTestCases+1):

        C, F, X = readRowAsFloats(filehandle)
        cookies = 0
        rate = 2
#        C = 500
#        F = 4
#        X = 2000
        farms = 0
        time = 0

        while True:
            currentTimeRemaining = X / float(rate)
            timeWithAdditionalFarm = (C / float(rate)) + (X / float(rate + F))
            if currentTimeRemaining >= timeWithAdditionalFarm:
                # Should buy farm
                timeToNextFarm = C / float(rate)
                time += timeToNextFarm
                rate += F
            else:
                timeToFinish = X / float(rate)
                time += timeToFinish
                break
        print "Case #{0}: {1:.10}".format(caseNumber, time)


if __name__ == "__main__":
    main()
