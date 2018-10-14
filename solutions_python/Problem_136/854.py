import sys
import math
import pdb
from decimal import *



def cookie(c, f, x):
    minn = x/2
    a = c/2
    s = 2 + f
    while True:
        curMin = a + x/s
        if curMin < minn:
            a = a + c/s
            minn = curMin
            s = s + f
        else:
            break

    return minn


if __name__=='__main__':

    fo = open("/Users/kushal/Downloads/B-large.in")
    
    tests = int(fo.readline().strip())
    for test in range(0,tests):
        values = fo.readline().split(' ')
        ans = cookie(Decimal(values[0]),Decimal(values[1]),Decimal(values[2]))
        print "Case #"+str(test+1)+": "+"%.7f"%ans



