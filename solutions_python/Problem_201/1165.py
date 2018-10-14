from heapq import*
from math import *

def solve(N,K):
    intervals = {N:1}
    lengths = [-N,0]

    while K>0:
        maxer = -lengths[0]
        numbs = intervals[maxer]

        L = (maxer-1)//2
        R = ceil((maxer-1)/2)

        if numbs >= K:
            return (R,L)

        K-=numbs
        intervals[maxer]=0
        heappop(lengths)
        if not L in intervals:
            heappush(lengths,-L)
            intervals.setdefault(L,0)
        if not R in intervals:
            heappush(lengths,-R)
            intervals.setdefault(R,0)
        
        intervals[L]+=numbs
        intervals[R]+=numbs


f = open("C-small-2-attempt0.in","r")
g = open("output.txt","w")

T = int(f.readline())

for i in range(1,T+1):
    [N,K] = [int(i) for i in f.readline().split()]

    # Solve
    (ans1,ans2) = solve(N,K)

    g.write("Case #{}: {} {}\n".format(i,ans1,ans2))

f.close()
g.close()
