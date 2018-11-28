#!/usr/bin/env python
import sys


sys.setrecursionlimit(5000)

def getmoves(state, flipper, flipped, flips=0):
    if(len(state) < flipper):
        for i, x in enumerate(state):
            if((x == '-' and flipped[i] % 2 != 1) or
               (x == '+' and flipped[i] % 2 != 0)):
                return None
        return flips
    if(state[0] == '+' and flipped[0] % 2 == 0):
        return getmoves(state[1:], flipper, flipped[1:] + [0], flips)
    if(state[0] == '-' and flipped[0] % 2 == 1):
        return getmoves(state[1:], flipper, flipped[1:] + [0], flips)
    for i in range(len(flipped)):
        flipped[i] += 1
    return getmoves(state[1:], flipper, flipped[1:] + [0], flips+1)
    # if(not untill):
    #     req = '+'
    # nreq = '-'
    # if(req == '-'):
    #     nreq = '+'
    # print state, req
    # if(len(state) < flipper):
    #     if(nreq in state[:untill]):
    #         return None
    #     if('-' in state[untill:]):
    #         return None
    # if(state[0] == req):
    #     return getmoves(state[1:], flipper, untill-1, req)
    # else:
    #     return getmoves(state[1:], flipper, flipper-1, nreq)


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for i in range(1, t+1):
    line = inFile.readline().strip().split(' ')
    state = line[0]
    flipper = int(line[1])
    ans = getmoves(state, flipper, [0]*flipper)
    if(ans is None):
        outFile.write("Case #{}: IMPOSSIBLE\n".format(i))
    else:
        outFile.write("Case #{}: {}\n".format(i, ans))
