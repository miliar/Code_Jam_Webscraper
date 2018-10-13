from math import ceil

def memoize(f):
    d = {}
    def func(*n):
        if n in d:
            return d[n]
        else:
            d[n] = f(*n)
            return d[n]
    return func

@memoize
def winning(a,b):
    if a<=0: return True
    if b<=0: return True
    if a==1 and b>1: return True
    if b==1 and a>1: return True
    
    maxk = int(ceil(b / a))
    for k in xrange(maxk,0,-1):
        if losing(a,b-k*a): return True
    maxk = int(ceil(a / b))
    for k in xrange(maxk,0,-1):
        if losing(a-k*b,b): return True
    return False
    
@memoize
def losing(a,b):
    if a<=0: return False
    if b<=0: return False
    
    maxk = int(ceil(b / a))
    for k in xrange(1,maxk+1):
        if not winning(a,b-k*a): return False
    maxk = int(ceil(a / b))
    for k in xrange(1,maxk+1):
        if not winning(a-k*b,b): return False
    return True
    

for i in xrange(1,int(raw_input())+1):
    a1,a2,b1,b2 = (int(x) for x in raw_input().split())
    count = 0
    for a in xrange(a1,a2+1):
        for b in xrange(b1,b2+1):
            if winning(a,b): count += 1
    print "Case #%d: %d" % (i,count)