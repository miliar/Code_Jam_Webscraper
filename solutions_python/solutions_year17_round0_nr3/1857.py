import heapq

def occupy(n,k):
    q = []
    heapq.heapify(q)
    heapq.heappush(q,0)

    for _ in range(k-1):
        if len(q)==0:
            return 0,0
        x = n-heapq.heappop(q)
        if x%2==1 and x/2>0:
            heapq.heappush(q,n-x/2)
            heapq.heappush(q,n-x/2)
        else:
            if x/2>0:
                heapq.heappush(q,n-x/2)
            if x/2>1:
                heapq.heappush(q,n-(x/2-1))
    
    if len(q)==0:
        return 0,0
    x = n-heapq.heappop(q)
    if x%2==1:
        return x/2, x/2
    else:
        return x/2, max(x/2-1,0)

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(T):
        n,k =  raw_input().split(" ")
        n = int(n)
        k = int(k)
        mx,mn = occupy(n,k)
        print "Case #{}: {} {}".format(t+1,mx,mn)
