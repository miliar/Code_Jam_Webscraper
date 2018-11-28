#!/usr/bin/python
import os, sys, math

# Return all recycled possibilities (not including self)
powers = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
def numDigits(n):
    numDigits = 1
    i = 0
    while n >= powers[i]:
        numDigits += 1
        i += 1
    return (numDigits, powers[i-1])

def recycled(n):
    if n < 10:
        return []
    (digits, lastPow) = numDigits(n)
    rs = [0 for i in range(digits-1)]
    for i in range(digits-1):
        lastDigit = n % 10
        n = lastDigit * lastPow + (n/10)
        if (lastDigit != 0):
            skip = False
            for j in range(i):
                if rs[j] == n:
                    skip = True
            if not skip:
                rs[i] = n
    return rs
        

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        caseStr = fileLines[index][:-1]
        index += 1
        (a, b) = [int(x) for x in caseStr.split(' ')]
        count = 0
        for i in xrange(a, b+1):
            for val in recycled(i):
                if (i < val and val <= b):
                    count += 1
        #print recycled(2341)
        #print recycled(200)
        #print recycled(12053)
        answer = count
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
