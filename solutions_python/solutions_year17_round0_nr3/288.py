import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for t in range(T):
    N, K = [int(i) for i in sys.stdin.readline().strip().split()]
    count = 0

    thing = deque()
    times = {}

    thing.appendleft(N)
    times[N] = 1

    while len(thing) != 0:
        thisSize = thing.pop()
        nextBig    = thisSize // 2
        nextSmall  = thisSize - 1 - nextBig

        thisTimes = times[thisSize]

        if nextBig in times:
            times[nextBig] += thisTimes
        else:
            thing.appendleft(nextBig)
            times[nextBig] = thisTimes

        if nextSmall in times:
            times[nextSmall] += thisTimes
        else:
            thing.appendleft(nextSmall)
            times[nextSmall] = thisTimes

        count += thisTimes

        if K <= count:
            print("Case #{}: {} {}".format(t+1, nextBig, nextSmall))
            break

