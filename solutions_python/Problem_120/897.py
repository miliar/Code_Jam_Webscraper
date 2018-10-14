import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print "Case #" + str(i) + ":",
    
    # read test case
    testCase = f.readline().split(' ')
    r = int(testCase[0])
    t = int(testCase[1])
    
    # check test case for row
    b = 2 * r -1
    hoge = b * b + 8 * t
    result = (int(sqrt(hoge)) - b) / 4
    print result
