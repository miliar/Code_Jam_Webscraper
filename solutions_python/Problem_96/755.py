"""Google code jam 2012 qual round problem B: Dancing"""

# Trick is to look mod 3.  Working out the cases, the remaining
# assignments can be done in greedy fashion based on how many
# "surprising" results are left.  N <= 100 so counting upto 100 OK.


import unittest
import operator
import sys

def solveIt(n,s,p,ti):
    # p is threshold
    ti.sort(reverse=True)
    ok = 0
    for k in ti:
        if k <= 1:
            if k >= p:
                ok += 1
            continue
        x = k / 3
        r = k % 3
        #print locals()
        if x >= p:
            ok += 1
            continue
        if (r != 0) and ((x+1) >= p):
            ok += 1
            continue
        if k < 2:
            continue
        if s <= 0:
            continue
        if (x > 2) and (r == 0) and ((x+1) >= p):
            ok += 1
            s -= 1
        if (r == 2) and ((x+2) >= p):
            ok += 1
            s -= 1
    return ok

def solveProblems(filename):
    f = open(filename, "r")
    l = f.readlines()
    f.close()
    l = map(lambda x: x[:-1], l)
    numCases = int(l[0])
    l = l[1:]
    for i in xrange(numCases):
        print >> sys.stderr, "Computing case %d" % (i + 1)
        a = l[i].split()
        n = int(a[0])
        s = int(a[1])
        p = int(a[2])
        ti = map(int, a[3:(3+n)])
        print "Case #%d: %d" % ((i + 1),solveIt(n,s,p,ti))

import getopt
def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "th", ["test", "help"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        #usage()
        sys.exit(2)
    for o, a in opts:
        if o in {"-t" : True, "--test" : True}:
            sys.argv = ["foo"] #+ args
            unittest.main()
            return
        elif o in {"-h" : True, "--help" : True}:
            #usage()
            sys.exit()
        else:
            assert False, "unhandled option"
    solveProblems(args[0])
 
if __name__ == "__main__":
    main()

# In:  
# Out: 
