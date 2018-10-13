from sortedcontainers import SortedList
from math import floor

def solve(data):
    n,k = map(int, data.rstrip().split())
    if n == k:
        return [0,0]
    l = SortedList()
    l.add(n)
    left = 0
    right = 0
    for i in range(k):
        curr = l.pop()
        left = int(floor(curr/2))
        right = curr - left - 1
        l.add(left)
        l.add(right)
    return sorted([left,right], reverse=True)

with open("C-small-2-attempt0.in") as f:
    T = int(f.readline().rstrip())
    data = f.readlines()
    ans = map(solve, data)
    i=0
    for sol in ans:
        i += 1
        print "Case #%d: %d %d" % (i,sol[0],sol[1])
    