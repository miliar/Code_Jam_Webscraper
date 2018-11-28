import sys
getint = lambda: int(raw_input())
getints = lambda: [float(z) for z in raw_input().split()]


def removeFirst(l):
    return l[:1]

def removeLast(l):
    return l[:-1]


for t in xrange(1, 1+getint()):
    N = getint()
    naomi = getints()
    naomi.sort()
    ken = getints()
    ken.sort()

    ken2 = [x for x in ken]
    naomi2 = [x for x in naomi]

    war = 0
    deceit = 0

    for i in xrange(N):
        xn = naomi[0]
        use = None
        for val in ken:
            if val > naomi[0]:
                use = val
                break
        if use:
            ken.remove(use)
        else:
            war += 1
        naomi = naomi[1:]

    for i in xrange(N):
        if naomi2[0] > ken2[0]:
            deceit += 1
            ken2 = ken2[1:]
        else:
            ken2 = ken2[:-1]
        naomi2 = naomi2[1:]




    print "Case #%d: %d %d" % (t, deceit, war)
