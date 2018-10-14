def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

for n in xrange(1,int(raw_input())+1):
    events = [int(x) for x in raw_input().split()][1:]
    minTime = max(events)
    t = 0
    for i,e in enumerate(events):
        t = gcd(t,minTime-e)
    print "Case #%d: %d" % (n,(t-minTime)%t)
