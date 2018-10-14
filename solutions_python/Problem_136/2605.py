rd=raw_input

def solve(c,f,x):
    def time(n):
        t=0.
        return x/(2+n*f) + sum(c/(2+i*f) for i in range(n))
    def low(n):
        return time(n)>time(n+1)

    lo,hi=0,1
    if not low(lo): return time(lo)
    else:
        while low(hi):
            lo=hi
            hi+=hi
        d = hi-lo
        while d > 1:
            d = d//2
            m = lo + d
            if low(m):
                lo = m
            else:
                hi = m
        return time(hi)

for t in range(1,1+int(rd())):
    c,f,x=map(float,rd().split())
    print 'Case #%d: %.7f'%(t,solve(c,f,x))

