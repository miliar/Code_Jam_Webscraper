from decimal import Decimal, getcontext
import sys


def solution(inFile):
    C, F, X = inFile.readline().rstrip().split(" ")
    C, F, X = Decimal(C), Decimal(F), Decimal(X)
    maxResult = X / Decimal(2)
    if X < C:
        return "%.7f" % maxResult

    lastCurrent = 99999999
    i = 1
    curF = Decimal(2)
    j = 0
    time = Decimal(0)
    while True:
        time += C / curF
        curF += F
        currentResult = time + Decimal(X / curF)
        i += 1
        if i == 2:
            if maxResult < currentResult:
                return "%.7f" % maxResult

        if lastCurrent < currentResult:
            break

        if currentResult <= maxResult:
            lastCurrent = maxResult
            maxResult = currentResult

    # print "%.7f" % maxResult
    return "%.7f" % maxResult


getcontext().prec = 15
inFile = open(sys.argv[1], "r")
outFile = open("out", "w")

N = int(inFile.readline())
for i in range(N):
    outFile.write("Case #%d: " % (i + 1))
    outFile.write(solution(inFile))
    outFile.write("\n")

inFile.close()
outFile.close()