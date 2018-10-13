def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return (a*b) / gcd(a,b)
    
T = int(raw_input())
for case in xrange(1,T+1):
    dates = map(int, raw_input().split())
    del dates[0]
    dates = list(set(dates))
    dates.sort()
    k = max(dates)
    factors = []
    for i in xrange(len(dates) -1):
        factors.append(dates[i+1] - dates[i])
    k = factors[0]
    for i in factors:
        k = gcd(k,i)
    best = k - (dates[0] % k)
    if best == k: best = 0
    print "Case #%d: %d" % (case, best)

