from bisect import insort_left
from heapq import heappop, heappush
def do_work(n, k):
    gaps = [n]
    a, b = None, None
    while k > 0:
        gap = gaps.pop()
        if gap % 2 == 0:
            a = gap//2
            b = a - 1
            if a > 0:
                insort_left(gaps, a)
            if b > 0:
                insort_left(gaps, b)
        else:
            a = gap//2
            b = a
            if a > 0:
                insort_left(gaps, a)
                insort_left(gaps, b)
        k -= 1
    return a, b

def do_work_2(n, k):
    h = [-n]
    a, b = None, None
    while k > 0:
        gap = heappop(h)
        gap = -gap
        if gap % 2 == 0:
            a = gap//2
            b = a - 1
            if a > 0:
                heappush(h, -a)
            if b > 0:
                heappush(h, -b)
        else:
            a = gap//2
            b = a
            if a > 0:
                heappush(h, -a)
                heappush(h, -b)
        k -= 1
    return a, b

# find lasta, lastb
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = input().split()
    n, k = int(n), int(k)
    a, b = do_work_2(n, k)
    print("Case #{}: {} {}".format(i, a, b))
