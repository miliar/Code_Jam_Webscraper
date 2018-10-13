import numpy as np
import sys


def evaluateLeadingTestCaseAndReturnNumberOFPossibleAnswer():
    global lines
    A, B, K = map(lambda x: int(x), lines[0].split(' '))
    lines = lines[1:] #Reset code lines for succeeding test cases

    wins = 0

    for i in range(0, A)[::-1]:
        for j in range(0, B)[::-1]:
            if (i&j) < K:
                wins += 1

    return wins



def returnFormattedAnswer(caseNum, x):
    g.write('Case #%d: %d\n' % (caseNum, x))

if __name__=='__main__':
    if len(sys.argv) != 3:
        print 'Provide arg1: input file, arg2: output file.'
    else:
        f = open(sys.argv[1])
        g = file(sys.argv[2], 'w')

        lines = map(lambda x: x.strip('\n'), f.readlines())
        numOfTestCases = int(lines.pop(0))

        for i in xrange(1, numOfTestCases + 1):
            returnFormattedAnswer(i, evaluateLeadingTestCaseAndReturnNumberOFPossibleAnswer())

        f.close()
        g.close()
