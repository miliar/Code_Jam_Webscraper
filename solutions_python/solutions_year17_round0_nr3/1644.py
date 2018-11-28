import heapq
import math

for I in range(int(input())):
    N, K = [int(n) for n in input().split(" ")]

    h=[]
    heapq.heappush(h,-N)

    for _ in range(K-1):
        m = -1*heapq.heappop(h)
        if m%2==0:
            m=math.floor(m/2)
            heapq.heappush(h,-(m-1))
            heapq.heappush(h,-m)
        else:
            m=math.floor(m/2)
            heapq.heappush(h,-m)
            heapq.heappush(h,-m)



    m = -1*heapq.heappop(h)
    l = r = 0
    if m%2==0:
        m=math.floor(m/2)
        l=m-1
        r=m
    else:
        m=math.floor(m/2)
        l=r=m

    print("Case #" + str(I+1) + ": "+ str(max(l,r)) + " " + str(min(l,r)))



        
    
    
    


