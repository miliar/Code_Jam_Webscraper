import numpy as np
import sys


def evaluateLeadingTestCaseAndReturnNumberOFPossibleAnswer():
    global lines
    currentTestCase = lines[:10]
    lines = lines[10:]
    res1 = int(currentTestCase[0])
    res2 = int(currentTestCase[5])
    t1 = currentTestCase[1:5]
    t2 = currentTestCase[6:10]
    r1 = t1[res1-1].split(' ')
    r2 = t2[res2-1].split(' ')
    return set(r1).intersection(r2)

def returnFormattedAnswer(caseNum, x):
    x = list(x)
    if 0 == len(x):
        g.write('Case #%d: Volunteer cheated!\n' % caseNum)
    elif 1 == len(x):
        g.write('Case #%d: %d\n' % (caseNum, int(x[0])))
    elif 1 < len(x):
        g.write('Case #%d: Bad magician!\n' % caseNum)


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