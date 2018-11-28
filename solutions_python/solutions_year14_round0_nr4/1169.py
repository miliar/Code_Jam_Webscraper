import numpy as np
import sys

def evaluateLeadingTestCaseAndReturnAnswer():
    global lines
    N = int(lines.pop(0))
    NaomiSetWar = sorted(map(lambda x: float(x), lines.pop(0).split(' ')))
    KenSetWar = sorted(map(lambda x: float(x), lines.pop(0).split(' ')))
    counterWar = 0

    NaomiSetDeceitfulWar = list(NaomiSetWar)
    KenSetDeceitfulWar = list(KenSetWar)
    counterDeceitfulWar = 0

    #Deceitful War
    if N == 1:
        if NaomiSetDeceitfulWar[0] < KenSetDeceitfulWar[0]:
            counterDeceitfulWar = 0
        else:
            counterDeceitfulWar = 1
    else:
        for i in xrange(N):
            n = NaomiSetDeceitfulWar.pop(0)
            if n < KenSetDeceitfulWar[0]:
                KenSetDeceitfulWar.pop(-1)
            else:
                KenSetDeceitfulWar.pop(0)
                counterDeceitfulWar += 1

    #War
    if N == 1:
        if NaomiSetWar[0] < KenSetWar[0]:
            counterWar = 0
        else:
            counterWar = 1
    else:
        for i in xrange(N):
            n = NaomiSetWar.pop(0)
            if n < KenSetWar[-1]:
                for j in KenSetWar:
                    if j > n:
                        KenSetWar.pop(KenSetWar.index(j))
                        break
            else:
                counterWar += len(NaomiSetWar) + 1
                break

    return (counterDeceitfulWar, counterWar)

def returnFormattedAnswer(caseNum, x):
    g.write('Case #%d: %d %d\n' % (caseNum, x[0], x[1]))


if __name__=='__main__':
    if len(sys.argv) != 3:
        print 'Provide arg1: input file, arg2: output file.'
    else:
        f = open(sys.argv[1])
        g = file(sys.argv[2], 'w')

        lines = map(lambda x: x.strip('\n'), f.readlines())
        numOfTestCases = int(lines.pop(0))

        for i in xrange(1, numOfTestCases + 1):
            returnFormattedAnswer(i, evaluateLeadingTestCaseAndReturnAnswer())

        f.close()
        g.close()