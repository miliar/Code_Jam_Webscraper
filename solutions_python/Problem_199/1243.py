#!/usr/bin/python3

import getopt
import sys
import math
import random

def flip(C,s,K):
    if s+K > len(C):
        return False
    
    for i in range(s,s+K):
        if C[i] == '-':
            C[i] = '+'
        else:
            C[i] = '-'

    return True

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
        A = f.readline().strip().split()
        cakes = list(A[0])
        K = int(A[1])

        counter = 0
        status = True
            
        # brute force
        for i in range(len(cakes)):
            if cakes[i] == '-':
                # flip that and the next K-2
                counter += 1
                status = flip(cakes,i,K)

        if not status:
            print("Case #%d: IMPOSSIBLE" % (c+1))
        else:
            print("Case #%d: %d" % (c+1, counter))




        

        




