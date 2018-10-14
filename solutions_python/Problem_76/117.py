#!/usr/local/bin/python

import sys;

def main():
    numCases = int(sys.stdin.readline().strip());
    for iCase in range(0, numCases):
        N =  int(sys.stdin.readline().strip());
        nums = [int(x) for x in sys.stdin.readline().strip().split()];
        if len(nums) != N:
            print >>sys.stderr, "invalid nums on case ", iCase;
            sys.exit(1);

        x = 0;
        for n in nums:
            x = x ^ n;

        if x != 0:
            print "Case #%d: NO" % (iCase + 1);
            continue;

        s = sum(nums);
        m = min(nums);
        print "Case #%d: %d" % (iCase + 1, s - m);

main();
