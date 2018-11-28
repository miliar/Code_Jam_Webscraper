#!/usr/bin/python

import sys;

def main():
    numCases = int(sys.stdin.readline().strip());
    for iCase in range(0, numCases):
        N =  int(sys.stdin.readline().strip());
        nums = [int(x) for x in sys.stdin.readline().strip().split()];
        if len(nums) != N:
            print >>sys.stderr, "invalid nums on case ", iCase;
            sys.exit(1);

        numNumsInPlace = 0;
        for i in range(0, N):
            if nums[i] == i + 1:
                numNumsInPlace += 1;
        print "Case #%d: %d.000000" % (iCase + 1, N - numNumsInPlace);

main();
