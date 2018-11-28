#
import os
import math

def solve(D,horses):
    maxm=0
    for horse in horses:
        time=(D-horse[0])/horse[1]
        maxm=max(maxm,time)
    speed=round(D/maxm,6)
    return speed

#print(solve(""))
