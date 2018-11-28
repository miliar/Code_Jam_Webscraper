

def f(n,p):
    p=2**n-p
    a = [0 for _ in xrange(n)]
    for k in xrange(n):
        if p%2==1:
            a[n-1-k]=1
        p/=2
    ln=0
    for g in a:
        if g==0:
            ln+=1
        else:
            break
    ret = 0
    for k in xrange(ln):
        ret += 2**(k+1)
    return min(ret, 2**n-1)


def g(n,p):
    a = [0 for _ in xrange(n+1)]
    for k in xrange(n+1):
        if p%2==1:
            a[n-k]=1
        p/=2
    ln=0
    for g in a:
        if g==0:
            ln+=1
        else:
            break
    #print a
    ret = 2**n-1
    for k in xrange(ln):
        ret -= 2**k
    return ret

def main():
    T=input()
    for t in xrange(T):
        cnt = 0
        n,p = map(int, raw_input().split())
        r1,r2 = f(n,p),g(n,p)
        print "Case #%s: %s %s"%(t+1,r1, r2)



main()