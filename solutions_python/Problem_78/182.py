import re
broken="Broken"
possible="Possible"

def getPosRange(d,n):
    if d==100 or d==0:
        return 1
    elif  d==50:
        if 2<n+1:
            return 2
        return 0
    elif d%25==0:
        if 4<n+1:
            return 4
        return 0
    elif d%20==0:
        if 5<n+1:
            return 5
        return 0
    elif d%10==0:
        if 10<n+1:
            return 10
        return 0
    elif d%5==0:
        if 20<n+1:
            return 20
        return 0
    elif d%4==0:
        if 25<n+1:
            return 25
        return 0
    elif d%2==0:
        if 50<n+1:
            return 50
        return 0
    else:
        if 100<n+1:
            return 100
        return 0

    
def solve(n,pd,pg):
    if pd==0 and pg<100:
        return possible
    if pd>=0 and pd<100 and pg==100 or pd>0 and pg==0:
        return broken
    posd=getPosRange(pd,n)
   # posg=getPosRange(pg,n)
    #print posd
    #print posg
    if posd>0:
        return possible
    return broken

file=open("a.in")
cs=int(file.readline())
for ii in range(1,cs+1):
    line=re.split(r"\s+",file.readline())
    n=int(line[0])
    pd=int(line[1])
    pg=int(line[2])
    res=solve(n,pd,pg)
    print "Case #%d: %s" % (ii,res)

