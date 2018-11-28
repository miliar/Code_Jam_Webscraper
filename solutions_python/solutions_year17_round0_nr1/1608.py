#!/usr/bin/env python3
# Oversized Pancake Flipper

# from sys import argv
import sys
sys.setrecursionlimit(2000)
TEST = False

# global variables and constants
TEST = False # not all caps

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

if TEST:
    pass

# K <= S
# something about where the divisions are?

# problem-specific defs

def flipCount(fliplist, flipsize, maxIndex, flipcount = 0):
    # odd number of flips -- not possible
    if len(fliplist) % 2 == 1:
        return -1 # i.e., not doable
    # nothing left to flip
    if len(fliplist) == 0:
        return flipcount
    else: # fliplist contains at least 2 elements
        fliplist.sort()
        # max - min of fliplist < S, then not possible?
        if fliplist[-1] - fliplist[0] < flipsize:
            return -1
        else:
            try:
                # print("fliplist", fliplist)
                flipEnd = fliplist.index(fliplist[0] + flipsize)
                # print("flipend", flipEnd)
                del fliplist[flipEnd] # this must go before next line
                fliplist = fliplist[1:]
                flipcount += 1
                # print("flipcount", flipcount)
                return flipCount(fliplist, flipsize, maxIndex, flipcount)
            except ValueError:
                # print("valueerror: fliplist", fliplist)
                if fliplist[0] + flipsize <= maxIndex:
                    fliplist[0] += flipsize
                    flipcount += 1
                    # print("flipcount", flipcount)
                    return flipCount(fliplist, flipsize, maxIndex, flipcount)
                else:
                    return -1
# main

# count flips, assuming position 0 and position S+1 are at +
# then need to pair up flip positions so as to be K apart, no remainders
# if possible, then count pairs, if not, then IMPOSSIBLE

T = int(input())

for tt in range(1, T+1): # for each test case
    tempS, tempK = input().split() # skip the explicit " "
    S = ['+'] + list(tempS) + ['+'] # prepend and append '+'
    K = int(tempK)

    # count discontinuities
    flips = [i for i in range(len(S)-1) if S[i] != S[i+1]] # list or set?
    # print(flips)

    #         printOutput(tt, 'IMPOSSIBLE')

    flips = flipCount(flips, K, len(S) - 1)

    if flips == -1:
        printOutput(tt, 'IMPOSSIBLE')
    else:
        printOutput(tt, str(flips))


    # recursion to handle +----+ 2 case?
    # if index doesn't exist, add
    # maybe re-sort and continue
    # even number of flips -- keep checking
    #
    # for ff in range(len(flips)-1):
    #     if flips[ff] >= 0:
    #         try:
    #             flipEnd = flips.index(flips[ff] + S)
    #         except ValueError:
    #             # result = 'IMPOSSIBLE' nope, see +----+ 2
    #             break
    #         flips[ff] = -1
    #         flips[flipEnd] = -1
    # else:
    #     result = str(int(len(flips)/2))

    # printOutput(tt, result)
            
    
    
