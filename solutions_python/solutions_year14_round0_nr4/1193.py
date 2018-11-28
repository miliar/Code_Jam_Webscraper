import sys

def ken_optim(ken, told):
    larger = filter(lambda x: x>told, ken)
    if len(larger) > 0:
        y = larger[0]
        larger.remove(y)
        return y
    return ken[0]

def naomi_optim_score(naomi, ken):
    s = 0
    sk = 0
    kl = len(ken) - 1
    nl = len(naomi) - 1
    while nl >= 0 and kl >= 0:
        if ken[kl] < naomi[nl]:
            s += 1
            kl -= 1
            nl -= 1
        else:
            kl -= 1
            sk += 1
    return s, sk

fp = sys.stdin

t = int(fp.readline())
for i in xrange(t):
    n = int(fp.readline())
    naomi = map(float, fp.readline().split())
    ken = map(float, fp.readline().split())

    naomi.sort()
    ken.sort()
    
    ds, dsk = naomi_optim_score(naomi, ken)
    sn, sk = 0, 0
    for x in naomi:
        y = ken_optim(ken, x)
        if x < y:
            sk += 1
        else:
            sn += 1
        ken.remove(y)
    #print 'Case #%d: %d %d, %d %d' % (i+1, ds, dsk, sn, sk)
    print 'Case #%d: %d %d' % (i+1, ds, sn)
