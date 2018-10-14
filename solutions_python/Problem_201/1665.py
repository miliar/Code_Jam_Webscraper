#!/usr/bin/env python3
# Bathroom Stalls

# from sys import argv
import collections
import math

# global variables and constants
TEST = False # not all caps

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

# problem-specific defs

if TEST:
    pass

# main
# K <= N
# odd vs even?
# list of occupied stalls
# also range of empty stalls (to check less, esp as everything gets full)
# track max gap?

# once K > N/2, then 
# max(min(Ls, Rs))
# min s for s in {max(min(Ls, Rs))}

# dict? gap size, count

T = int(input())

for tt in range(1, T+1): # for each test case
    N, K = [int(x) for x in input().split()]

    # use try/except and dict or defaultdict
    # gapDict = {}
    # or use Counter (collections.Counter)...
    
    # this approach does not maintain all the tie-breaking rules --
    # are they actually necessary?

    # print('K, N', K, N)
    # if K > N/1.5:
    #     printOutput(tt, '0 0') # check
    #     continue

    gapCount = collections.Counter({N : 1})
    # print(gapCount)

    # # version 1: fine for small dataset 1
    # # if gapcount[gapsize] = 0, then use del
    # for kk in range(1,K): # figure out how to do this in chunks
    #     # maybe do chunks when there is a del gapCount
    #     maxGap = max(gapCount.elements()) # must delete keys with value 0
    #     if maxGap == 1:
    #         printOutput(tt, '0 0')
    #         # print(N, kk)
    #         break
    #     y = math.ceil((maxGap - 1)/2)
    #     if y > 0: # omit gaps of size 0 -- this seems a wee bit faster
    #         gapCount[y] += 1
    #         z = math.floor((maxGap - 1)/2)
    #         if z > 0:
    #             gapCount[z] += 1
    #     if gapCount[maxGap] == 1: # or <= 1? but might hide errors
    #         del gapCount[maxGap]
    #     else:
    #         gapCount[maxGap] -= 1
    #     # print(gapCount)
    # else:
    #     maxGap = max(gapCount.elements()) # must delete keys with value 0
    #     y = math.ceil((maxGap - 1)/2)
    #     z = math.floor((maxGap - 1)/2)
    #     printOutput(tt, str(y) + ' ' + str(z))

    # version 2: in chunks
    # if gapcount[gapsize] = 0, then use del
    kk = 0
    y = z = N
    # ll = 0
    # print('K', K)
    while kk < K: # < ?
    # while kk < K and ll < 20: # < ?
        # print('kk', kk)
        # ll += 1
        # maybe do chunks when there is a del gapCount?
        maxGap = max(gapCount.elements()) # must delete keys with value 0
        # print('gapCount', gapCount)
        if maxGap == 1:
            # print('maxgap of 1')
            y = z = 0
            # print(N, kk)
            break
        # print('if maxgap = 1, then this should not be printed')

        gapJump = min(gapCount[maxGap], K - kk)
        y = math.ceil((maxGap - 1)/2)
        if y > 0: # update only non-zero gaps
            gapCount[y] += gapJump
            z = math.floor((maxGap - 1)/2)
            if z > 0:
                gapCount[z] += gapJump

        # print(y, z)

        # print('gapcount stuff', gapCount, K - kk)
        # print(maxGap, gapJump, kk)
        kk += gapJump
        gapCount[maxGap] -= gapJump
        if gapCount[maxGap] == 0:
            del gapCount[maxGap] # does this matter? only at kk = K

    printOutput(tt, str(y) + ' ' + str(z))
                
    # y = math.ceil((maxGap - 1)/2)
    # if y > 0: # omit gaps of size 0 -- this seems a wee bit faster
    #     gapCount[y] += 1
    #     z = math.floor((maxGap - 1)/2)
    #     if z > 0:
    #         gapCount[z] += 1
    #     if gapCount[maxGap] == 1: # or <= 1? but might hide errors
    #         del gapCount[maxGap]
    #     else:
    #         gapCount[maxGap] -= 1
    #     # print(gapCount)
    # else:
    #     maxGap = max(gapCount.elements()) # must delete keys with value 0
    #     y = math.ceil((maxGap - 1)/2)
    #     z = math.floor((maxGap - 1)/2)
    #     printOutput(tt, str(y) + ' ' + str(z))

