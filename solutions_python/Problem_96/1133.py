#!/usr/bin/python

import sys;
import os.path; 
THIS_DIR = os.path.dirname(sys.argv[0]);
sys.path.append(THIS_DIR + '/..')
from util import *;

def main():
    nt = readi();
    for t in range(1, nt+1):
        nums = readia();
        (n, s, p) = nums[:3];
        info = [];
        for a in nums[3:]:
            aDiv3 = a / 3;
            aMod3 = a % 3;
            if aMod3 == 0: # 9 = 3 + 3 + 3 or 2 + 3 + 4
                maxSimple = aDiv3;
                if aDiv3 > 0:
                    maxSurp = aDiv3 + 1;
                else:
                    maxSurp = -1;
            elif aMod3 == 1: # 10 = 3 + 3 + 4 or 2 + 4 + 4
                maxSimple = aDiv3 + 1
                if aDiv3 > 0:
                    maxSurp = aDiv3 + 1;
                else:
                    maxSurp = -1;
            else: # aMod3 == 2   11 = 3 + 4 + 4 or 3 + 3 + 5
                maxSimple = aDiv3 + 1
                maxSurp = aDiv3 + 2

            info.append((a, maxSimple, maxSurp))

        info.sort();
        info.reverse();
        #print info;

        numMoreP = 0;
        numSurpLeft = s;
        for (a, maxSimple, maxSurp) in info:
            if maxSimple >= p:
                numMoreP += 1;
            elif maxSurp >= p and numSurpLeft > 0:
                numMoreP += 1;
                numSurpLeft -= 1;

        print "Case #%d: %d" % (t, numMoreP);


main();
