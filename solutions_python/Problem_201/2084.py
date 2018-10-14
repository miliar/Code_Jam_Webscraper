"none"
import fileinput
import math
import heapq


def test():
    "none"
    assert solve(2, 2) == (0, 0)
    assert solve(5, 4) == (0, 0)
    assert solve(6, 4) == (0, 0)
    assert solve(6, 3) == (1, 0)
    assert solve(1000, 1) == (500, 499)
    assert solve(1000, 2) == solve(500, 1)
    assert solve(395, 391) == solve_simple(395, 391)

def solve(size, people):
    "none"
    thresh = math.ceil(size / 2.0)
    if people > thresh:
        return 0, 0
    if people == size:
        return 0, 0

    h = []
    num = size
    A, B = 0, 0
    while people > 0:
        N = num / 2
        if num % 2 == 0: #even
            heapq.heappush(h, -N)
            heapq.heappush(h, -max(0, N-1))
            A, B = max(N, max(0, N-1)), min(N, max(0, N-1))
        else:
            heapq.heappush(h, N)
            heapq.heappush(h, N)
            A, B = N, N
        # print num, q, people
        people -= 1
        if people == 0:
            break
        num = -heapq.heappop(h)
            
    return A, B

def solve_simple(size, people):
    h = [-size]
    A, B = 0, 0
    while people > 0:
        num = -heapq.heappop(h)
        N = num / 2
        if num % 2 == 0: #even
            heapq.heappush(h, -N)
            heapq.heappush(h, -max(0, N - 1))
            A, B = max(N, max(0, N-1)), min(N, max(0, N-1))
        else:
            heapq.heappush(h, -N)
            heapq.heappush(h, -N)
            A, B = N, N
        people -= 1
    return max(A, B), min(A, B)

test()

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    N, size = line.strip().split(" ")
    res = solve_simple(int(N), int(size))
    if res is None:
        res = "IMPOSSIBLE"
    print "Case #%d: %s %s " % (i, res[0], res[1])
    # print N, size, solve(int(N), int(size)), solve_simple(int(N), int(size))

# for i in xrange(1, 100):
#     for j in xrange(1, 10**9):
#         pass
#     print i, j

"""
# 0 . . 0
"""