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
        N,K = [int(x) for x in f.readline().split()]

        # find path to element K
        level = 1
        current = 1

        while True:
            Nleft = math.floor((N-1) / 2)
            Nright = math.ceil((N-1) / 2)

            if verbose:
                print("at %d (%d, %d, %d): ? %d" % (current, N, Nleft, Nright,
                                                    K)) 
            
            if K == current:
                break
            if K & level:
                # go left
                current += 2*level
                N = Nleft
            else:
                # right
                current += level
                N = Nright
            level <<= 1

        
        print("Case #%d: %d %d" % (c+1, Nright, Nleft))





        

        




