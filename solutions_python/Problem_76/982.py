from __future__ import generators
import sys
from sys import stdin 
import string

#def xcombinations(items, n):
    #if n==0: yield []
    #else:
        #for i in xrange(len(items)):
            #for cc in xcombinations(items[:i]+items[i+1:],n-1):
                #yield [items[i]]+cc

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def sumSean(candies):
    sum = 0
    for i in candies:
        sum += i

    return sum

def sumPatrick(candies):
    sum = 0
    for i in candies:
        sum = sum ^ i

    return sum

def checkSolutions(candies):
    seanMax = 0
    for i in range(1, len(candies)):
        #print >> sys.stderr, "checking candies: " + str(i) + " to " + str(len(candies)-i)
        for c in xcombinations(range(len(candies)), i):
            take = []
            leave = []
            for j in range(len(candies)):
                if j in c:
                    #print >> sys.stderr, "taking " + str(candies[j])
                    take.append(candies[j])
                else:
                    #print >> sys.stderr, "leaving " + str(candies[j])
                    leave.append(candies[j])
            #print >> sys.stderr, "take: " + str(take) + " sum: " + str(sumSean(take)) + " sum patrick : " + str(sumPatrick(take))
            #print >> sys.stderr, "leave: " + str(leave) + " sum: " + str(sumSean(leave)) + " sum patrick : " + str(sumPatrick(leave))
            if sumPatrick(take) == sumPatrick(leave):
                #print >> sys.stderr, "take: " + str(take) + " sum: " + str(sumSean(take)) + " sum patrick : " + str(sumPatrick(take))
                #print >> sys.stderr, "leave: " + str(leave) + " sum: " + str(sumSean(leave)) + " sum patrick : " + str(sumPatrick(leave))
                s = max(sumSean(take), sumSean(leave))
                if s > seanMax:
                    seanMax = s
    print >> sys.stderr, "sean takes: " + str(seanMax)
    return seanMax


def main():
    #for p in xcombinations(['l','o','v','e'], 3): print p
    numOfCases = int(stdin.readline())
    for i in range(0, numOfCases):
        #if i > 3:
            #sys.exit()
        print >> sys.stderr, "case " + str(i)
        numOfCandies = int(stdin.readline())
        l = stdin.readline().split()
        c = []
        for k in l:
            c.append(int(k))
        #s = checkSolutions(c)
        #print (checkSolutions(c))
        #result = "NO"
        #if s > 0:
            #result = str(result)
        s = checkSolutions(c);
        result = "NO"
        if s > 0:
            result = str(s)

        print "Case #" + str((i+1)) + ": " + result



if __name__ == "__main__":
    main()
