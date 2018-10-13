#
# Google Code Jam 2010
# (C) Andrew Tutt
#
# Code Jam Skeleton
#

from time import sleep, clock
import os

from copy import copy
import math

IN_FILENAME = 'input.txt'
OUT_FILENAME = 'output.txt'

def solver(L,P,C):
    # Can Support L People
    # Cannot support P People
    # Within a factor of C
    # How many tests?

    if L * C >= P: return 0

    # In the worst Case, a site can support
    # L people
    
    # for 1 1000 2 : in the worst case the site supports 1 person
    # We test 64: if we make 64 we test 128: etc.
    # 63, 125, 250, 500, Done
    # 64, 32, 16, 8, 4, 2, Done
    # 2, 4, 8, 16, 32, 64, 128, 256, 512
    # Test 64
    # Test 256 or 16
    # Test 32 or 4
    # Test 8 or 2

    count = 0
    while(True):
        count += 1
        P = P / C
        if L >= P: break

    return math.ceil(math.log(count,2))

##    oldP = copy(P)
##
##    count = 0
##    while(True):
##        count += 1
##        # Do a worst test
##        P = P / C
##        L = L * C
##        print((P,L))
##        if L >= P: break
##        if count > 1:
##            if L * C >= P: break

    # Count now has the worst worst case scenario
    # We now take that scenario and divide equally between
    # the up and down cases

    return count

if __name__ == '__main__':
    clock()
    f = open(IN_FILENAME, 'r')
    total_cases = int(f.readline())

    t_range = range(1,total_cases+1)
    olist = list(range(1,total_cases+2))

    # Read in the problems
    for case_number in t_range:
        L, P, C = f.readline().strip().split(' ')
        olist[case_number] = solver(int(L),int(P),int(C))
        #print(olist[case_number])

    f = open(OUT_FILENAME, 'w')
    for c in t_range:
        f.write("Case #" + str(c) + ": " + str(olist[c])+"\n")
        #print("Case #" + str(c) + ": " + str(olist[c]))

    print(str(clock()) + " seconds")

