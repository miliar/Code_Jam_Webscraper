#!/usr/bin/python3

import getopt
import sys

def seed_cache(maxrange):
    cc = [[0 for y in range(maxrange)] for x in range(maxrange)]

    for i in range(2, maxrange):
        for j in range(1, i):
            cc[i][j] = 1 + cc[i-j][j]

    return cc

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

    maxr = 1001
    cc = seed_cache(maxr)

    for c in range(ncases):
        D = int(f.readline().strip())
        P = [int(x) for x in f.readline().split()]

        best = 100000
        for fac in range(1, maxr):
            b = fac
            for i in P:
                b += cc[i][fac]
            if b < best:
                best = b

        print("Case #%d: %d" % (c+1, best))





        

        




