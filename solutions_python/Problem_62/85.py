from m_util import *
import bisect

T = int(raw_input())

for c in range(1, T + 1):
    N = int(raw_input())
    p = []
    alist = []
    blist = []
    
    for _ in range(N):
        a,b = map(int, raw_input().split())
        alist.append((a,len(p)))
        blist.append((b,len(p)))
        p.append([a,b])
        
    alist.sort()
    blist.sort()
    
    bIndList = [b for b,i in blist]
    
    #print alist,blist,p
    ans = 0
    for a,i in alist:  
        bInd = bisect.bisect(bIndList, p[i][1])
        for b,j in blist[:bInd]:
            if(i!=j and p[j][0] >= a):
                #print i,j,bInd
                ans+=1
    
    #if(len(p) == 2 and (p[0][0]>=p[1][0] and p[0][1]<=p[1][1]
    #                    or p[0][0]<=p[1][0] and p[0][1]>=p[1][1])):       
    #    ans = 1
    
    
    print "Case #%d: %s" % (c, ans)
    