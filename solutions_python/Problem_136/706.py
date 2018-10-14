import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print "Case #" + str(i) + ":",
    
    # read test case
    testCase = f.readline().split(' ')
    C = float(testCase[0])
    F = float(testCase[1])
    X = float(testCase[2])

    sec = 0.0
    cookies = 0.0
    perSec = 2.0
    while cookies < X :
        if (X / perSec) <= (C / perSec) + (X / (perSec + F)) :
            sec += X / perSec
            break
        else :
            sec += C / perSec
            perSec += F
    print sec
