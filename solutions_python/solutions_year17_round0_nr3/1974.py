# A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.
#
# Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible.
# To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS,
# each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively.
# Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal.
# If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal.
# If there are still multiple tied stalls, they choose the leftmost stall among those.
#
# K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.
#
# When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

# input: T [test cases] followed by rows of "N K"
# we return the max(LS, RS) and min(LS, RS) values for the last person we enter

# brute force it?

from collections import deque
DEBUG = False
for T in range(1, int(input()) + 1):

    x = 0
    y = 0

    n, k = [int(x) for x in input().split()]
    config = deque('o')
    config.extend([ '.' for __ in range(n)])
    config.append('o')
    # n = 5 let's say and k=2
    # config = o . . . . . o
    mid = 0 # EDIT: don't initializelen(config) / 2 # rounds down so will get leftmost
    mids = [] # EDIT: don't initialize#[mid]
    for person in range(k):
        # find the greatest number of periods in our list?
        # brute force: simply do a linear search xD
        # correct: do a binary search, go through mids and divide it up
        # for now, linear search

        #
        #
        largestPeriods = 0
        startIndex = 0
        currentPeriods = 0
        currentStart = 0
        for i in range(len(config)):
            if config[i] == '.':
                currentPeriods += 1
                if currentPeriods > largestPeriods:
                    startIndex = currentStart
                    largestPeriods = currentPeriods
            else:
                currentStart = i+1
                currentPeriods = 0
        # ok, we got our startIndex and the number of periods in a row
        # this one will be the leftmost of those
        if largestPeriods % 2 == 0:
            mid = startIndex + int(largestPeriods / 2) - 1
        else:
            mid = startIndex + int(largestPeriods / 2)
        # mid = startIndex + int(largestPeriods / 2)
        mids.append(mid)
        config[mid] = 'o'
        if DEBUG:
            print(list(config))
            print(mid)
        if person == k - 1:
            # we need to calculate x & y
            # make list of .'s with length largestPeriods
            mList = ['.' for x in range(largestPeriods)]
            # middle of it is mid - startIndex
            middleOfmList = mid-startIndex
            if DEBUG:
                mList[middleOfmList] = 'o'
                print(mList)
            # number on left
            leftSide = len(mList[:middleOfmList])
            # number on right
            rightSide = len(mList[middleOfmList + 1:])
            x = max(leftSide, rightSide)
            y = min(leftSide, rightSide)

            if DEBUG:
                print ("Right side: " + str(rightSide))
    print("Case #" + str(T) + ": " + str(x) + " " + str(y))

