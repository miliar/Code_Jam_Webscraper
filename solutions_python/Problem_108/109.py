import sys
import math
import heapq

T = int(sys.stdin.readline())

for case in range(1, T + 1) :
    output = "Case #" + str(case) + ": "
    line = sys.stdin.readline().strip().split(" ")
    N = int(line[0])
    v = []
    for i in range(N):
        line = sys.stdin.readline().strip().split(" ")
        v.append([int(line[0]), int(line[1])])
    line = sys.stdin.readline().strip().split(" ")
    D = int(line[0])

    def canReach (startPos, endPos, length):
        if startPost + length <= endPos:
            return startPos + length - endPos
        else:
            return None

    checked = {}
#    steps = []
    result = False
#    if v[0][0] < v[0][1]:
    steps = [ [-(v[0][0] + v[0][0]), v[0][0], v[0][0]], ]
    while len(steps) > 0:
        if result:
            break
        step = heapq.heappop(steps)
        if tuple(step) in checked:
            continue
#        print "I grab", step
        for _ in v:
            if step[1] + step[2] >= D:
                result = True
                break
            if step[1] <= _[0] <= step[1] + step[2]:
                if _[0] - step[1] > 0:
#                    print "I can grab", _
                    heapq.heappush(steps, [-(_[0] + min(_[1], _[0] - step[1])), _[0], min(_[1], _[0] - step[1])])
        checked[tuple(step)] = 1
    print output + ("YES" if result else  "NO")
