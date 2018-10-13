import sys
import os
from math import sqrt

SQRT_5 = sqrt(5)

def run_case(handle):
    n = int(handle.readline().strip())
    value = ((3+SQRT_5)**n)%1000
    return ("000"+str(value).split('.')[0])[-3:]

def main():
    handle = open(sys.argv[1])
    testcases = int(handle.readline())
    for i in range(testcases):
        print "Case #%d: %s" % (i+1, run_case(handle))

if __name__ == '__main__':
    main()
