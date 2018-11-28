def split(m,sp):
    sp.sort()
    n = sp[-1]
    if n/2 + n%2 + 1 >=n:
        return (m,sp)
    sp.pop()
    sps = [split(m+1,sp+[i,n-i]) for i in range(n/2+n%2,n-1)]+[(m,sp+[n])]
    return min(sps,key = lambda (t,sp): t+max(sp))

for case in range(1,int(raw_input())+1):
    D = int(raw_input())
    Ps = map(int,raw_input().split())
    m,sp = split(0,Ps)
    print "Case #%d: %d" % (case,m+max(sp))
