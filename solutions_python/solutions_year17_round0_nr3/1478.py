import sys
import math

def parse():
    NT = int(input())

    testCases = []
    for i in range(1, NT + 1):
        n, k = input().split(" ")
        testCases.append((int(n), int(k)))
    return testCases


def getMaxAndMin(n, k):
    # Figure out the lengths of the remaining empty stalls
    # Represent empty stalls using numbers
    emptyStalls = dict()
    emptyStalls[n] = 1
    lastMax = None
    for i in range(k):
        # Split the list into two parts while removing an element
        maxList = max(emptyStalls.keys())
        if maxList == 0:
            return 0, 0
        # Decrement the count or remove the key
        if emptyStalls[maxList] > 1:
            emptyStalls[maxList] = emptyStalls[maxList] - 1
        else:
            emptyStalls.pop(maxList, None)

        L1, L2 = int(math.floor((maxList-1)/2)), int(math.ceil((maxList-1)/2))
        if L1 in emptyStalls:
            emptyStalls[L1] = emptyStalls[L1] + 1
        else:
            emptyStalls[L1] = 1

        if L2 in emptyStalls:
            emptyStalls[L2] = emptyStalls[L2] + 1
        else:
            emptyStalls[L2] = 1
        # print("Empty Stalls list={0}, i={0}".format(emptyStalls, i))
        lastMax = maxList

    # print("Last Max = {0}".format(lastMax))
    # NOTE: The empty stall list is bounded on both sides, either by body gaurds or by
    #       users

    # Last list that was split had odd length => center is the solution we seek
    if lastMax % 2 != 0:
        LS = int(math.ceil(lastMax/2)) - 1      # Note: LS == RS in this case
        return LS, LS
    else:
        LS = [lastMax/2 - 1, lastMax/2]
        RS = LS[::-1]

        minLsRs = []
        maxLsRs = []
        for ls, rs in zip(LS, RS):
            if ls < rs:
                minLsRs.append(ls)
                maxLsRs.append(rs)
            elif ls == rs:
                minLsRs.append(ls)
                maxLsRs.append(rs)
            else:
                minLsRs.append(rs)
                maxLsRs.append(ls)

        # Which point do we want?
        # By default, assume it is the first center
        idx = 0
        if minLsRs[0] < minLsRs[1]:
            idx = 1
        elif minLsRs[0] == minLsRs[1]:
            if maxLsRs[0] < maxLsRs[1]:
                idx = 1

        return int(maxLsRs[idx]), int(minLsRs[idx])



def main():
    testCases = parse()
    for i, t in enumerate(testCases):
        solution = getMaxAndMin(*t)
        print("Case #{0}: {1} {2}".format(i+1, *solution))

if __name__ == '__main__':
    main()
