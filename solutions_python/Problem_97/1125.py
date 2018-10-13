#!/usr/bin/python

import sys;
import os.path; 
THIS_DIR = os.path.dirname(sys.argv[0]);
sys.path.append(THIS_DIR + '/..')
from util import *;

def recycle(n, B):
    #print "recycle ", n;
    res = 0;
    digits = str(n);
    used = set();
    for i in range(len(digits)):
        dig2 = digits[i:] + digits[:i]
        m = int(dig2);
        #print m;
        if n < m and m <= B and m not in used:
            #print n, m;
            used.add(m);
            res += 1;
    return res;

def main():
    nt = readi();
    for t in range(1, nt+1):
        (A, B) = readia();
        numRecycled = 0;
        for n in xrange(A, B + 1):
            numRecycled += recycle(n, B);

        print "Case #%d: %d" % (t, numRecycled);
    

main();
