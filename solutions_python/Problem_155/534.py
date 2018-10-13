#!/usr/bin/python3

import getopt
import sys

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
        i1,i2 = f.readline().split()
        S = int(i1)
        A = [int(x) for x in list(i2)]

        friends, count = 0, 0
        for l in range(S):
            count += A[l]
            if not(count + friends > l):
                friends += (l+1)- (count + friends)
        
        print("Case #%d: %d" % (c+1, friends))





        

        




