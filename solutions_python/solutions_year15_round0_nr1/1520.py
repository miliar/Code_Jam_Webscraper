#!/usr/bin/env python2

import sys

def readinput(f):
    test_cases = int(f.readline())
    for ncase in range(test_cases):
        max_shy, s = f.readline().split(' ')
        num, af = 0, 0
        for i in range(int(max_shy) + 1):
            c = s[i]
            if num < i:
                af += i - num
                num = i
            i+=1
            num += int(c)
        print "Case #%d: %d" % (ncase + 1, af)



if __name__=="__main__":
    readinput(sys.stdin)
