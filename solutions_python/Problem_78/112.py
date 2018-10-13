import sys, re
from fractions import Fraction

def ispos(testcase):
    # prepare input
    dstack = []

    if (testcase[2] == 100):
        if (testcase[1] == 100): return "Possible"
        else: return "Broken"
    
    if (testcase[2] == 0):
        if (testcase[1] == 0): return "Possible"
        else: return "Broken"
    
    a = Fraction(testcase[1],100)
    if (a.denominator <= testcase[0]): return "Possible"
    else: return "Broken"
       


def processtestcases():
    numtestcases = int(sys.stdin.readline().rstrip())
    testcases = []
    
    # read in instructions for each test case
    for i in range(numtestcases):
        inputs = sys.stdin.readline().rstrip().split(' ')

        # 3 items
        testcases.append([int(inputs[0]),int(inputs[1]),int(inputs[2])])

    return testcases


if __name__ == "__main__":
    testcases = processtestcases()
    #print str(testcases)
    i = 1
    for testcase in testcases:
        ispossible = ispos(testcase)
        print "Case #"+str(i)+": "+ispossible
        i += 1





