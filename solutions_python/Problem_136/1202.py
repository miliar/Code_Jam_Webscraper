import numpy as np
import sys
#Condition for critical rate::
# C/(Rc) + X / (Rc + F) >= X/Rc

def evaluateLeadingTestCaseAndReturnAnswer():
    global lines
    C, F, X = map(lambda x: float(x), lines.pop(0).split(' '))

    timeEvaluator = lambda n: C/(2.0 + (n-1)*F)

    lhs = lambda n: (C/(2.0+(n-1)*F)) + (X/(2.0+(n*F)))
    rhs = lambda n: X/(2.0 + (n-1)*F)

    counter = 1
    while lhs(counter) < rhs(counter):
        counter += 1

    t = 0

    for i in xrange(counter - 1): #do not include last count, it should be evaluated using rhs
        t += timeEvaluator(i + 1)

    t += rhs(counter)

    return t

def returnFormattedAnswer(caseNum, x):
    g.write('Case #%d: %.7f\n' % (caseNum, x))


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