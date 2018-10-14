"""Google code jam qual round problem A: speaking in tongues."""

# Since it's the same for the real input as for the examples, just
# generate the dictionary once and always look up the result.

import unittest
import operator
import sys

givenInput=[
    "a",
    "o",
    "z",
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    "q"
    ]
givenOutput=[
    "y",
    "e",
    "q",
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "z"
    ]
givenEx=zip(givenInput, givenOutput)

outputToInput={}

def addPairOfStr(inputStr, outputStr):
    for (cIn,cOut) in zip(inputStr, outputStr):
        if outputToInput.has_key(cOut):
            if outputToInput[cOut] != cIn:
                print "For char %s: %s %s" % (cOut, cIn, outputToInput[cOut])
        outputToInput[cOut]=cIn
for (s,t) in givenEx:
    addPairOfStr(s,t)

def showRemaining(l):
    for i in xrange(ord('a'), ord('z')+1):
        if chr(i) not in l:
            print "Missing %c" % chr(i)
def showProgress():
    print "Found %d elements" % len(outputToInput.keys())
    print "Outputs"
    showRemaining(outputToInput.keys())
    print ""
    print "Inputs"
    showRemaining(outputToInput.values())

def solveIt(s):
    x = map(lambda c: outputToInput[c], s)
    return "".join(x)

def solveProblems(filename):
    f = open(filename, "r")
    l = f.readlines()
    f.close()
    l = map(lambda x: x[:-1], l)
    numCases = int(l[0])
    l = l[1:]
    for i in xrange(numCases):
        print >> sys.stderr, "Computing case %d" % (i + 1)
        print "Case #%d: %s" % ((i + 1),solveIt(l[i]))

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
