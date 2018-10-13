#!/usr/bin/env python
"""
Pancakes.py -- solution to inf. pancakes problem in Code Jam 2015

"""

sol_cache = dict() # For memoization
def recSol(D, Parr):
    """ Recursive implementation of solve """
    if Parr[0] <= 1:
        return 1
    else:
        if tuple(Parr) not in sol_cache.keys():
            retval = Parr[0]
            x = Parr[0]//2
            for i in range(1,x+1):
                new_Parr = (Parr[1:]+[i,Parr[0]-i])
                new_Parr.sort(reverse=True)
                retval = min(retval,
                             1+recSol(D+1,new_Parr))
            sol_cache[tuple(Parr)]=retval
        return sol_cache[tuple(Parr)]
    
def solve(D, Parr):
    """ Entry point for computing the friends """
    Parr.sort(reverse=True)
    return recSol(D, Parr)
    
    
if __name__=="__main__":
    import sys,ntpath
    filename = input()
    fileout = input()
    with open(filename, "r") as instream:
        sys.stdin = instream
        outstream = open(fileout, "w")
        sys.stdout = outstream
        for i in range(int(input())):
            D = int(input())
            P = list(map(int, input().split(" ")))
            print("Case #{}: {}".format(i+1,solve(D,P)))
        outstream.close()
