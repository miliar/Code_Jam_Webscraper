#!/usr/bin/env python3

from itertools import chain

T = int(input().strip())

for t in range(T):
    print("Case #{}: ".format(t + 1), end="\n")
    H, W = map(int, input().strip().split(" "))
    cakeInitially = [input() for _ in range(H)]
    lineGroupSizes = []
    lastLineGroupSize = 0
    lineGroups = []
    for line in cakeInitially:
        lastLineGroupSize += 1
        if line != "?"*W:
            lineGroups.append(line)
            lineGroupSizes.append(lastLineGroupSize)
            lastLineGroupSize = 0
    lineGroupSizes[-1] += lastLineGroupSize

    modifiedLineGroups = []
    for lineGroup in lineGroups:
        groupSizes = []
        lastGroupSize = 0
        groups = []
        for letter in lineGroup:
            lastGroupSize += 1
            if letter != "?":
                groups.append(letter)
                groupSizes.append(lastGroupSize)
                lastGroupSize = 0
        groupSizes[-1] += lastGroupSize
        modifiedLineGroups.append(''.join(groupSize * letter for groupSize, letter in zip(groupSizes, groups)))
    print('\n'.join(chain.from_iterable(groupSize * [group] for groupSize, group in zip(lineGroupSizes, modifiedLineGroups))))

