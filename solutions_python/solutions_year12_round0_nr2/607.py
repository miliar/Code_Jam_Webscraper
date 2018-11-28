#!/usr/bin/python
import os, sys, math

def solve(S, p, scores):
    #classes[0] = too low to hit p
    #classes[1] = can hit p if surprising
    #classes[2] = always can hit p w/o surprising
    classes = [0, 0, 0]
    if p == 0:
        return len(scores)
    if p == 1:
        count = 0
        for score in scores:
            if score > 0:
                count += 1
        return count
    for score in scores:
        if score < (3 * p - 4):
            classes[0] += 1
        elif score < (3 * p - 2):
            classes[1] += 1
        else:
            classes[2] += 1
    return classes[2] + min(classes[1], S)

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        caseStr = fileLines[index][:-1]
        index += 1
        nums = [int(x) for x in caseStr.split(' ')]
        N = nums[0]
        S = nums[1]
        p = nums[2]
        scores = nums[3:]
        if len(scores) != N:
            print "BAD NUMBER OF SCORES case %d" % caseNum
            sys.exit(1)
        answer = solve(S, p, scores)
        #print caseStr
        print "Case #%d: %d" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
