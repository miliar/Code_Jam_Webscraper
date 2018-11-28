import math
from sortedcontainers import SortedList
f = open('B-small-practice.in', 'r')
T = int(f.readline())
def bathroom_stall(i):
    emptyspace = SortedList()    
    N, K  = [int(x) for x in f.readline().strip().split()]
    emptyspace.add(N)
    temp, mid = 0, 0
    for k in range(K):
        temp = emptyspace.pop()
        mid = (temp + 1) // 2
        emptyspace.add(mid - 1)
        emptyspace.add(temp - mid)
    print ('Case #%d: %d %d' % (i+1, temp - mid, mid -1))




for i in range(T):
    bathroom_stall(i)