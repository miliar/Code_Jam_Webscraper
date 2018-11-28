#!/usr/bin/env python3

from collections import deque

# this is the urinal protocol as described by Randall Munroe

T = int(input().strip())

def addToDeq(freeRanges, width, count):
    if len(freeRanges) > 0 and freeRanges[-1][0] == width:
        freeRanges[-1][1] += count
    else:
        freeRanges.append([width, count])

for t in range(T):
    print("Case #{}: ".format(t + 1), end="")
    
    stalls, people = map(int, input().strip().split(" "))
    
    freeRanges = deque(([stalls, 1],))
    
    while True:
        currentWidth, currentCount = freeRanges.popleft()
        if people > currentCount:
            addToDeq(freeRanges, currentWidth//2, currentCount)
            addToDeq(freeRanges, (currentWidth - 1)//2, currentCount)
            people -= currentCount
        else:
            print("{} {}".format(currentWidth//2, (currentWidth - 1)//2))
            break

