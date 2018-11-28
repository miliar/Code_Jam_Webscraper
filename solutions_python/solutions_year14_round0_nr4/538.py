#!/usr/bin/env python

import sys, os, re

#---------------------------------------------------
# Variable 
#---------------------------------------------------

#---------------------------------------------------
# Function 
#---------------------------------------------------
def war(alist, blist):
    alist.sort()
    blist.sort()

    score = 0
    while len(alist) > 0:
        v = alist[0]
        del alist[0]

        if v > blist[-1]:
            score += 1
            del blist[0]
        else:
            for i in range(len(blist)):
                if blist[i] > v:
                    del blist[i]
                    break
    return score

def cheat_war(alist, blist):
    alist.sort()
    blist.sort()

    score = 0
    while len(alist) > 0:
        if alist[0] > blist[0]:
            score += 1
            del alist[0]
            del blist[0]
        else:
            del alist[0]
            del blist[-1]
    return score


def load_file(filename):
    with open(filename, 'rU') as f:
        number = int(f.readline())
        for n in range(number):
            length = int(f.readline())
            alist = [ float(s) for s in f.readline().strip().split(' ')[:length]]
            blist = [ float(s) for s in f.readline().strip().split(' ')[:length]]
            alist1 = alist[:]
            blist1 = blist[:]

            s0 = cheat_war(alist, blist)
            s1 = war(alist1, blist1)
            print "Case #%d: %d %d" % (n+1, s0, s1)
    return

#---------------------------------------------------
# Entry Point 
#---------------------------------------------------
def main():
    load_file (sys.argv[1])
    #print check_cookie(30., 1., 2.)
    #print check_cookie(30., 2., 100.)
    #print check_cookie(30.5, 3.14159, 1999.19990)
    #print check_cookie(500, 4.0, 2000.0)

    return

#---------------------------------------------------
# Unit Test Entry 
#---------------------------------------------------
if __name__ == '__main__':
    main()


