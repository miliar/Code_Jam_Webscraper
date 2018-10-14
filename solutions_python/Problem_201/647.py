import sys
import time
from heapq import heappush, heappop

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    N,K = readlist()
    heap = []
    dic = {}

    def add(n, c):
        if n<2:
            n = 1
        mi,ma = -((n-1)//2),-(n//2)
        dic[(mi,ma)] = dic.get((mi,ma),0)+c
        heappush(heap, (mi,ma))

    def get():
        mi,ma = heappop(heap)
        while len(heap)>0 and heap[0] == (mi,ma):
            heappop(heap)
        c = dic[(mi,ma)]
        del dic[(mi,ma)]
        return (-mi,-ma,c)

    add(N,1)
    while True:
        mi,ma,c = get()
        K -= c
        if K<=0:
            return str(ma) + ' ' + str(mi)
        add(mi,c)
        add(ma,c)


start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
