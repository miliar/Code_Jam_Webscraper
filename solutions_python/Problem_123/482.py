#!/usr/bin/env python
from __future__ import division
import os, sys, math

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False

# number of test cases
line = input_file.readline().strip()
K = int(line)

def g(s,m):
    return (2**m)*s - (2**m - 1)


# f(s,j,v,n) = minimal # of moves to finish game, if you have size s, starting with jth competitor
def f(s,j,v,n):
    # print "debug: %d,%d" % (s, j)
    if (s<=1): # tiny sum
        return n-j
    elif (j==(n-1)): # last position
        if v[j] < s:
            return 0 # absorb
        else:
            return 1 # drop
    else:      

        if s > v[j]: # absorb
            return f(s+v[j],j+1,v,n)
        else:
            # compute number of adds to absorb
            adds = 0
            t = s
            while t <= v[j]: 
                t += t-1
                adds += 1

            # target = v[j]
            # lo = 1
            # hi = v[j] - s + 1
            # m = (lo+hi)/2
            # while lo <= hi:
            #     m = (lo+hi)/2
            #     if g(s,m) > target && g(s,m-1) > target # go down
            #         hi = m-1
            #     elif g(s,m) < target # go up
            #         lo = m+1
            #     else:
            #         break
            # if t == -1:
            #     sys.exit("ERROR")
            # s = g(s,m)
    
            # return min(m + f(s+v[j],j+1,v,n), 1 + f(s,j+1,v,n))            

            # either add and absorb, or drop
            return min(adds + f(t+v[j],j+1,v,n), 1 + f(s,j+1,v,n))

# main method
def main():

    # process each case
    for k in xrange(0,K):
        # read input
        line = input_file.readline().strip()        
        a,n = map(int,line.split())
        line = input_file.readline().strip()        
        v = map(int,line.split()) # sizes
        v.sort()

        moves = f(a,0,v,n)

        # return answer
        print "Case #%d: %d" % (k+1,moves)

if __name__ == '__main__':
    main()