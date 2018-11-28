#!/usr/bin/env python
"""
Ovation.py -- solution to ovation problem in Code Jam 2015

"""

def solve(smax, sarr):
    """ Entry point for computing the friends """
    friends = 0
    standing = 0
    for shyness,people in enumerate(map(int, sarr)):
        if standing < shyness:
            friends += shyness - standing
            standing = shyness # Update standing
        standing += people # adding shy people also
    return friends
    
if __name__=="__main__":
    import sys,ntpath
    filename = input()
    fileout = input()
    with open(filename, "r") as instream:
        sys.stdin = instream
        outstream = open(fileout, "w")
        sys.stdout = outstream
        for i in range(int(input())):
            x,y = input().split(" ")
            print("Case #{}: {}".format(i+1,solve(x,y)))
        outstream.close()
