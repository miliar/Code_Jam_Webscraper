def gl(f, splitchar=' '):
    return map(f, raw_input().split(splitchar))

def g(f):
    return f(raw_input())

def timeToNextFarm(c,f,x,n,r):
    return max((c-n)/r, 0.0)

def timeToCompletion(c,f,x,n,r):
    return max((x-n)/r, 0.0)

def timeToCompletionWithNextFarm(c,f,x,n,r):
    return timeToNextFarm(c,f,x,n,r) + timeToCompletion(c,f,x,max(n-c,0),r+f)

t=g(int)
for i in xrange(t):
    c,f,x=gl(float)
    n=0
    r=2.0
    tot = 0.0
    while True:
        if timeToCompletionWithNextFarm(c,f,x,n,r) < timeToCompletion(c,f,x,n,r):
            tot += timeToNextFarm(c,f,x,n,r)
            r += f
        else:
            tot += timeToCompletion(c,f,x,n,r)
            break
    print "Case #%d: %.7f" % (i+1, tot)
