#!/usr/bin/python

import sys;
import os.path; 
from collections import *;
from Queue import *;

def readi():
    return int(sys.stdin.readline().strip());

def readia():
    return [int(x) for x in sys.stdin.readline().strip().split()];

def readfa():
    return [float(x) for x in sys.stdin.readline().strip().split()];

def reads():
    return sys.stdin.readline().strip();

def mergeAndCountInvs(left, right, cmpf):
    merged = [];
    numInvs = 0;
    iLeft = 0;
    iRight = 0;
    while iLeft < len(left) and iRight < len(right):
        nLeft = left[iLeft];
        nRight = right[iRight];
        if (cmpf(nLeft, nRight) < 0):
            merged.append(nLeft);
        else:
            merged.append(nRight);
        #merged.append(min(right[iRight], left[iLeft]))
        if cmpf(nRight, nLeft) < 0:
            numInvs += len(left) - iLeft;
            iRight += 1;
        else:
            iLeft += 1;
    merged += left[iLeft:] + right[iRight:];
    return numInvs, merged;

def sortAndCountInvs(nums, cmpf):
    if len(nums) <= 1:
        return 0, nums;
    n = len(nums) // 2; 
    left = nums[:n];
    right = nums[n:];
    resLeft, left = sortAndCountInvs(left, cmpf);
    resRight, right = sortAndCountInvs(right, cmpf);
    res, nums1 = mergeAndCountInvs(left, right, cmpf);
    return resLeft + resRight + res, nums1;

def main():
    #print sortAndCountInvs([], cmp);
    #print sortAndCountInvs([5, 4, 2, 3], cmp);
    #print sortAndCountInvs([5, 4, 2, 3], lambda x, y: -cmp(x, y));
    nt = readi();
    for t in range(1, nt+1):
        N = readi();
        nums = readia();
        if len(nums) != N:
            print >>sys.stderr, "BAD"

        M = 1 << N;
        minOps = N * N * N;
        bestPerm = 0;
        bestFlags = [];
        bestFlags1 = [];
        bestNumsLeft = [];
        bestNumsRight = [];
        bestSTD = 0;
        bestNOL = 0;
        bestNOR = 0;

        for perm in xrange(M):
            # zeros go left
            middle = 0;
            i = 1;
            j = 0;
            flags = [];
            numsLeft = [];
            numsRight = [];
            while i < M:
                if perm & i == 0:
                    middle += 1;
                    flags.append(0);
                    numsLeft.append(nums[j]);
                else:
                    flags.append(1);
                    numsRight.append(nums[j]);
                i <<= 1;
                j += 1;
            numStepsToDivide, flags1 = sortAndCountInvs(flags, cmp);
            #print "perm: ", perm, ", flags: ", flags, ", stepsToDiv: ", numStepsToDivide,  ", flags1: ", flags1;
            #print "numsLeft: ", numsLeft, ", numsRight: ", numsRight;
            numOpsLeft, sortedLeft = sortAndCountInvs(numsLeft, cmp);
            numOpsRight, sortedRight = sortAndCountInvs(numsRight, lambda x, y: cmp(y, x));
            numOps = numStepsToDivide + numOpsLeft + numOpsRight;
            if numOps < minOps:
                minOps = numOps;
                bestPerm = perm;
                bestFlags = flags[:];
                bestFlags1 = flags1[:];
                bestNumsLeft = numsLeft[:];
                bestNumsRight = numsRight[:];
                bestSTD = numStepsToDivide;
                bestNOL = numOpsLeft;
                bestNOR = numOpsRight;


        #print "nums: ", nums;
        #print "bestPerm: ", bestPerm, ", bestFlags: ", bestFlags,  ", bestNumsLeft: ", bestNumsLeft, ", bestNumsRight: ", bestNumsRight;
        #print "bestSTD: ", bestSTD, ", bestNOL: ", bestNOL, ", bestNOR: ", bestNOR;

        #bestMiddle = 0;
        #for middle in xrange(N + 1):
        #    nums1 = nums[:];
        #    invsLeft, numsLeft = sortAndCountInvs(nums1[:middle], cmp);
        #    invsRight, numsRight = sortAndCountInvs(nums1[middle:], lambda x, y: cmp(y, x));
        #    if invsLeft + invsRight < minOps:
        #        minOps = invsLeft + invsRight;
        #        bestMiddle = middle;

        #print "best middle: ", bestMiddle;
        #print "nums: ", nums;


        print "Case #%d: %d" % (t, minOps);
    

main();
