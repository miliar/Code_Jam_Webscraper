from  math import *
T = int(input())
for t in range(1,T+1):
    n, k = map(int,input().split())
    p = []
    maxr = 0
    rr = []
    for i in range(n):
        r, h = map(int,input().split())
        p.append((h*r,r))
        rr.append((r,h))
    p.sort(reverse = True)
    rr.sort(reverse = True)
    ansh  =  0
    maxr = 0
    for i in range(k):
        ansh += p[i][0]
        if p[i][1] > maxr:
            maxr = p[i][1]
    ans = 2*pi*ansh + pi*maxr*maxr
    
    mr = p[k-1][0]
    for el in rr:
        if el[0] > maxr:
            if 2*mr + maxr*maxr < 2*el[0]*el[1] + el[0]*el[0]:
                ans = ans - pi*(2*mr + maxr*maxr - 2*el[0]*el[1] - el[0]*el[0])
                mr = el[0]*el[1]
                maxr = el[0]
    print('Case #'+str(t)+':', ans)
        