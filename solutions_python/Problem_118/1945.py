import sys
from math import sqrt, ceil
f = open(sys.argv[1], 'r')

# Number of test cases
numOfTests = int(f.readline())

for i in range(1, numOfTests + 1) :
    print "Case #" + str(i) + ":",

    # Read test case
    testCase = f.readline().split(' ')
    testCase[0] = int(testCase[0])
    testCase[1] = int(testCase[1])

    testAns = 0
    for i in range(int(ceil(sqrt(testCase[0]))), int(sqrt(testCase[1])) + 1) :
        testStr = str(i)

        # Test for fair
        for j in range(len(testStr) / 2) :
            if testStr[j] != testStr[-j-1] :
                break
        else :
            testStr = str(i * i)
            for j in range(len(testStr) / 2) :
                if testStr[j] != testStr[-j-1] :
                    break
            else :
                testAns += 1

    print testAns
