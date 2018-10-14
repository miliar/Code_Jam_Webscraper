#!/usr/bin/python3

import getopt
import sys
import math

if __name__ == "__main__":

    verbose = False
    fname = "input.txt"

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:",
                                   ["verbose","help","input="])
    except getopt.GetoptError as err:
        print (str(err)) 
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"): sys.exit()
        elif o in ("-v", "--verbose"): verbose = True
        elif o in ("-f", "--input"): fname = a
        else: sys.exit()

    f = open(fname, "rt")
    ncases = int(f.readline())

    for c in range(ncases):
        X, R, C = [int(x) for x in f.readline().split()]

        Gabriel = False
        
        if verbose:
            print("Case %d: %d-omino on %d x %d" % (c+1, X, R, C))

        if X == 1:
            Gabriel = True
        elif X == 2:
            if (R*C/2 == int(R*C/2)):
                Gabriel = True
        elif X == 3:
            if((R*C/3 == int(R*C/3)) and R*C > 3):
                Gabriel = True
        elif X == 4:
            if(R*C >= 12):
                Gabriel = True
        else:
            print("Didn't see that")

        r = "GABRIEL" if Gabriel else "RICHARD"

        print("Case #%d: %s" % (c+1,r))





        

        




