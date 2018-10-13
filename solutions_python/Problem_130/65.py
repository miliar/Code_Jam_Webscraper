testcases = int(raw_input())

def log2(n):
    if (n == 0):
        return 0
    r = 0
    p = 1
    while (p <= (n+1)):
        r += 1
        p *= 2
    return (r-1)

def guaranteed(n,p):
    dn = 2 ** n
    if (dn == p):
        return (dn-1)
    ajoute = dn/2
    perdu = ajoute
    defaitesok = 1
    while (perdu < p):
        ajoute /= 2
        perdu += ajoute
        defaitesok += 1
    personnesderriere = 2**defaitesok - 1
    return personnesderriere - 1

def could(n,p):
    dn = 2 ** n
    q = 1
    m = 0
    while (dn / q > p):
        q *= 2
        m += 1
    # m = min(truc)
    return (dn - q)

for case in xrange(1,testcases+1):
    n,p = raw_input().split()
    n = int(n)
    p = int(p)
    print "Case #%d: %d %d" % (case,guaranteed(n,p),could(n,p))
