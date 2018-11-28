#!/usr/bin/python3

#$Id:$

# Google code jam 2014
# problem 2

import time
import getopt
import sys

def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print ('%s took %0.2f s' % (func.__name__, (t2-t1)))
        return res
    return wrapper

def usage():
    print('''
    Magic trick (task 1)

Options:
-h (--help) 
-v (--verbose)
''')


if __name__ == "__main__":

    verbose = False
    fname = "input.txt"
    # r is the standard cookie production per s
    r = 2.0

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:",
                                   ["verbose","help","input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-f", "--input"):
            fname = a
        else:
            usage()
            sys.exit()


    # reading input
    # first line: number of test cases. T cases follow
    # each test case:
    # one line containing three floats C, F, X
    # C : costs of a farm
    # F : farm production
    # X : cookies needed to win
    # sample:
    # 4
    # 30.0 1.0 2.0
    # 30.0 2.0 100.0
    # 30.50000 3.14159 1999.19990
    # 500.0 4.0 2000.0

    f = open(fname, "rt")
    ncases = int(f.readline())
    if verbose:
        print("%s: %d cases." % (fname, ncases))

    for c in range(ncases):
        C, F, X = [float(x) for x in f.readline().split()] 

        if verbose:
            print("Case %d: C: %.5f F: %.5f X: %.5f" % (c, C, F, X))

        # solve it: 
        # First, how many farms are needed can be determined by that 
        # expression: 
        # X/C - r/F  = n 
        # The smallest integer <= n is the number of farms needed in 
        # optimum scenario

        # could be a rounding issue here
        n = max(0, int(X/C - r/F))

        if verbose:
            print("Will need %d farms" % (n))

        # now, calculate the time needed based on n farms
        # example for 3 farms:
        # total = C/2 + C/(2+1*F)+ C/(2+2*F) + X/(2+3*F)
        total = 0.0
        for i in range(n):
            total = total + C/(r+i*F)

        total = total + X / (r+n*F)

        # output
        print ("Case #%d: %.7f" % (c+1, total))


        



        

        




