import numpy as np
import scipy
import math
import heapq


nt = int(raw_input())

def solve(n,k,r,hw):
    h = []
    in_heap = 0
    sumw = 0
    ans = 0
    for i in xrange(n):
        si = math.pi*r[i]*(2*hw[i] + r[i])
        
        if in_heap >= k-1:
           ans = max(ans, 2*math.pi*sumw + si)
        
        w = r[i]*hw[i]
        if in_heap < k-1 or (len(h) > 0 and w > h[0]):
            if in_heap == k-1:
                sumw -= heapq.heappop(h)
                in_heap -= 1            
            sumw += w
            heapq.heappush(h,w)
            in_heap += 1
    
    return ans
            
        
    
for i_it in xrange(nt):
    ans = 0
    n,k = map(int, raw_input().split())
    v = []
    
    for i in xrange(n):
        ri,hi = map(int,raw_input().split())
        v.append((ri,hi))
        
    v.sort()
    r = [x[0] for x in v]
    h = [x[1] for x in v]
    
    ans = solve(n,k,r,h)
        
    print "Case #{}: {}".format(i_it+1,ans)
    
