from fractions import gcd

def solve():    
    n,l,h = map(int,raw_input().split())
    f = map(int,raw_input().split())
    f.sort()
    g = [0]*n
    g[n-1]=f[n-1]
    for i in reversed(xrange(n-1)):
        g[i]=gcd(g[i+1],f[i])
    nk = 1
    m = h+1
    for i in xrange(n):
        nd = g[i]
        if nd%nk==0:
            k = nk*(l/nk)
            if k<l: k+=nk
            if k<=h and k<=nd:
                m = min(k,m)                
        nk = f[i]*nk/gcd(f[i],nk)
    for i in xrange(l,h+1):
        for x in f:
            if not(x%i==0 or i%x==0): break
        else:
            break        
    else:
        i = None    
    r2 = i
    r1 = (m if m<=h else None)
    #if r1!=r2: print 'BOTVA', r1,r2
    return r2
    
    
t = input()
for tn in xrange(t):
    r = solve()
    print "Case #%d:"%(tn+1),
    if r is None: print "NO"
    else: print r
