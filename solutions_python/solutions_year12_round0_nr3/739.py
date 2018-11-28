"""Google code jam 2012 qual round problem C: recycled numbers"""

# try counting solution first

import unittest
import operator
import sys

def solveIt(aStr, bStr):
    numDigits = len(aStr)
    a = int(aStr)
    b = int(bStr)
    count = 0
    for i in xrange(a, b+1):
        h = {}
        s = "%d" % i
        for r in xrange(numDigits):
            t = s[r:] + s[:r]
            tInt = int(t)
            if (tInt < a) or (tInt > b):
                continue
            if tInt < i:
                h = {}  # already counted
                break
            h[tInt] = True
        k = len(h.keys())
        if k >= 2:
            #print i, h.keys()
            count += ((k * (k - 1)) / 2)
    return count

def solveProblems(filename):
    f = open(filename, "r")
    l = f.readlines()
    f.close()
    l = map(lambda x: x[:-1], l)
    numCases = int(l[0])
    l = l[1:]
    for i in xrange(numCases):
        print >> sys.stderr, "Computing case %d" % (i + 1)
        (aStr,bStr) = l[i].split()
        print "Case #%d: %d" % ((i + 1),solveIt(aStr, bStr))

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
