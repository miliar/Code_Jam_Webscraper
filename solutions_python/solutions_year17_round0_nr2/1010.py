def solve(n):
    s=str(n)
    l=list(s)
    nines=0
    for x in range(len(l)):
        if nines:
            l[x]='9'
        elif x<len(l)-1 and l[x]>l[x+1]:
            l[x]=str(int(s[x])-1)
            nines=1

    n=int(''.join(l))
    if nines:
        return solve(n)        
            
    else:
        return n
            
            
            
def go(fn):
    f=open(fn)
    cases=int(f.readline())
    for c in range(1,cases+1):
        n=f.readline()
        r=solve(int(n))
        print 'Case #%d: %d'%(c,r)
    f.close()
              
go('B-large.in')
