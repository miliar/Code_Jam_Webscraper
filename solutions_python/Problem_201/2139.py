from heapq import heapify,heappush,heappop

def solve(N,K):
    heap=[(-N,0)]

    for i in range(K-1):
        nowL,nowPos=heappop(heap)

        l=(-nowL)//2
        if nowL % 2:
            heappush(heap,(-l,nowPos))
            heappush(heap,(-l,nowPos+l))
        else:
            heappush(heap,(-(l-1),nowPos))
            heappush(heap,(-l,nowPos+1))
        
    lastL,lastPos=heappop(heap)
    l=(-lastL)//2

    return (l,l) if lastL % 2 else (l,l-1)

T=int(input())
for i in range(T):
    N,K=map(int,input().split())

    print('Case #{}: {} {}'.format(i+1,*solve(N,K)))
