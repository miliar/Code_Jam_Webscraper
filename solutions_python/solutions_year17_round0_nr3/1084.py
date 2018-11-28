from collections import deque
from heapq import heappop, heappush

def solve():
    n, k = map(int, str(input()).rstrip().split())
    q = []
    heappush(q, -n)
    while k > 1:
        x = -heappop(q) - 1
        if x == 0:
            return (0, 0)
        if x % 2 == 0:
            heappush(q, -(x // 2))
            heappush(q, -(x // 2))
        else:
            heappush(q, -(x // 2 + 1))
            heappush(q, -(x // 2))
        k -= 1
    x = -heappop(q)
    x -= 1
    if x % 2 == 0:
        return (x // 2, x // 2)
    else:
        return (x // 2 + 1, x // 2)

if __name__ == '__main__':
    t = int(str(input()).rstrip())
    for i in range(1, t + 1):
        a, b = solve()
        print('Case #' + str(i) + ': ' + str(a) + ' ' + str(b))
