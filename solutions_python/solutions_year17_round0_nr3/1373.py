#!/usr/local/bin/python3
import queue as Q
from heapq import heappush, heappop

t = int(input())
for cs in range(1,t+1):
    #q = Q.PriorityQueue()
    hq = []
    n,k = list(map(int, input().split()))
#    q.put((-n,0,(0,n-1)))
    heappush(hq,(-n,0,(0,n-1)))
    for i in range(1,k):
#        it = q.get()
        it = heappop(hq)
        mid = int((it[2][0]+it[2][1])/2)
#        print(it, mid)
#        q.put((-(mid-it[2][0]),it[2][0], (it[2][0],mid-1)))
#        q.put((-(it[2][1]-mid),mid+1, (mid+1,it[2][1])))
        heappush(hq,(-(mid-it[2][0]),it[2][0], (it[2][0],mid-1)))
        heappush(hq,(-(it[2][1]-mid),mid+1, (mid+1,it[2][1])))
#    it = q.get()
    it = heappop(hq)
    mid = int((it[2][0]+it[2][1])/2)
#    print(it, mid)
    mi, mx = min(mid-it[2][0], it[2][1]-mid), max(mid-it[2][0], it[2][1]-mid)
    print("Case #%d: %d %d"%(cs,mx,mi)) 
