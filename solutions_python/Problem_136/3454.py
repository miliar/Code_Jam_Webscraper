__author__ = 'mac'

import sys
OUTPUT_STRING = "Case #{0}: {1:.7f}\n"

sys.setrecursionlimit(30000)



def decide(C,F,X, cookieRate):
    stay = X/cookieRate
    buy = C/cookieRate + X/(cookieRate+F)
    if stay < buy:
        return stay
    else:
        return C/cookieRate + decide(C,F,X, cookieRate+F)


def runTestCase(f):
    cookieRate = 2
    C,F,X = [float(x) for x in f.readline().split()]
    return decide(C,F,X,cookieRate)



with open('B-small-attempt0.in','r') as f, open("out.txt",'w') as outF:
    numTests = int(f.readline())
    for i in range(0,numTests):
        outF.write(OUTPUT_STRING.format(i+1,runTestCase(f)))
