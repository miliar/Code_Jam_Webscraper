import heapq

def updateHeapAndMap(h,m,size,countAdd):
    if size in m:
        m[size] = m[size] + countAdd
    else:
        heapq.heappush(h,-size)
        m[size] = countAdd

def seat_visitors(N,K):
    pl = K
    h = []
    m = {}
    heapq.heappush(h,-N)
    m[N] = 1
    while pl > 0:
        mx = -heapq.heappop(h)
        count = m[mx]
        del m[mx]
        pl -= count
        size = int(mx/2)
        if mx % 2:
            updateHeapAndMap(h,m,size,count*2)
            if pl <= 0:
                return (size,size)
        else:
            updateHeapAndMap(h,m,size,count)
            updateHeapAndMap(h,m,size - 1,count)
            if pl <= 0:
                return (size, size - 1)


num_tests = int(input())
for i in range(1, num_tests + 1):
    n, k = [int(s) for s in input().split(" ")]
    results = seat_visitors(n,k)
    print("Case #{}: {} {}".format(i,results[0],results[1]))
