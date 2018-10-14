from heapq import *

for t in range(int(input())):
    n, k = [int(item) for item in input().split()]
    st = [- n]
    for i in range(k - 1):
        p = - heappop(st)
        if p % 2 == 0:
            heappush(st, - (p // 2))
            heappush(st, - (p // 2 - 1) )
        else:
            heappush(st, - (p // 2))
            heappush(st, - (p // 2))
    
    ans = - heappop(st)
    if ans % 2 != 0:
        y = z = ans // 2
    else:
        y = ans // 2
        z = ans // 2 - 1
    
    print("Case #{}: {} {}".format(t + 1, y, z))