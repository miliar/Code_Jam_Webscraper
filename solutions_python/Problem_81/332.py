def WP2OWP(a, WP, oc):
    OWP = []
    for (item,opponents) in zip(a, oc):
        s = 0.0
        i = 0
        for c in item:
            if c != '.':
                s += (WP[i] * oc[i] -1 + int(c)) / (oc[i] - 1)
            i += 1
        OWP.append(s / opponents)
    return OWP

def OWP2OOWP(a, WP, oc):
    OWP = []
    for (item,opponents) in zip(a, oc):
        s = 0.0
        i = 0
        for c in item:
            if c != '.':
                s += (WP[i])
            i += 1
        OWP.append(s / opponents)
    return OWP
    
    
def solve(a):
    n = len(a)
    oc = map(lambda item: len(item)-item.count('.'), a)
    # compute WP
    WP = []
    for item in a:
        WP.append(float(item.count('1')) / (item.count('1') + item.count('0')))
        
    OWP = WP2OWP(a, WP, oc)
    OOWP = OWP2OOWP(a, OWP, oc)
    
    result = map(lambda i: 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i], xrange(n))
    for item in result:
        print item
        
t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    a = []
    for j in xrange(n):
        a.append(raw_input())
    print "Case #%d:" % (i+1)
    solve(a)
    
