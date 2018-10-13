import math
import heapq

f = open('input.txt', 'r')
out = open('output.txt', 'w') 
n = int(f.readline())

def solve(n, k):
    h = [-n]
    for i in xrange(k):
        maxt = -heapq.heappop(h)
        second = int(math.ceil((maxt - 1) / 2.0))
        last = (maxt - 1) / 2
        if second == 0 and last == 0:
            return 0, 0
        heapq.heappush(h, -second)
        heapq.heappush(h, -last)

    return second, last

def solve2(n, k):
    first = [n]
    second = [None] * (len(first)*2)
    for i in xrange(k):
        max_first = max(first)
        if max_first == -1:
            first, second = second, [None] * (len(second)*2)
            max_first = max(first)
        max_first_idx = first.index(max_first)
        first[max_first_idx] = -1
        second[max_first_idx*2] = (max_first - 1) / 2
        second[max_first_idx*2+1] = int(math.ceil((max_first - 1) / 2.0))

    return second[max_first_idx*2+1], second[max_first_idx*2]

for i in xrange(n):
    n, k = f.readline().split()
    ans = solve(int(n), int(k))
    out.write("Case #%d: %s %s\n" % (i+1, ans[0], ans[1]))

    
