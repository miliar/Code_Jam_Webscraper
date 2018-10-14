import sys
import math
import heapq


def parse(instrm):
    n, k = instrm.readline().rstrip().split()
    return int(n), int(k)


def solve(case):
    n, k = case
    s = [-n]
    mins = None
    maxs = None
    for i in range(k):
        half = (-heapq.heappop(s)-1)/2
        mins = math.floor(half)
        maxs = math.ceil(half)
        if maxs > 0:
            heapq.heappush(s, -maxs)
            if mins > 0:
                heapq.heappush(s, -mins)
    return "{} {}".format(maxs, mins)


if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve(case)
            print("Case #{}: {}".format(i+1, ans))
