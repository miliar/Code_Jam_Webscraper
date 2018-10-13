import math
for yu in range (int(input())):
    q,w=list(map(int,input().strip().split()))
    if w!=q:
        r=[q]
        c=[]
        ri=0
        while ri<len(r):
            if r[ri]!=0:
                p=[math.ceil((r[ri]-1)/2),math.floor((r[ri]-1)/2)]
                c+=[p]
                r+=p
            ri+=1
        c=sorted(c)
        c.reverse()
        print('Case #'+str(yu+1)+':',c[w-1][0],c[w-1][1])

    else:
        print('Case #'+str(yu+1)+':',0,0)
    
 
