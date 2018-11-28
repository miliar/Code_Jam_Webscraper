import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    naomi = [float(x) for x in f.readline().split()]
    ken = [float(x) for x in f.readline().split()]
    naomi.sort()
    ken.sort()

    # war
    war = 0
    k = ken[:]
    n = naomi[:]
    while k and n:
        n_bar = n.pop(0)
        for j in range(len(k)):
            if k[j] > n_bar:
                k.pop(j)
                break
        else:
            k.pop(0)
            war += 1

    # deceit
    deceit = 0
    k = ken[:]
    n = naomi[:]
    while k and n:
        n_bar = n.pop(0)
        if n_bar < k[0]:
            k.pop(len(k) - 1)
            continue
        deceit += 1
        k.pop(0)

    print "Case #%d: %d %d" % (t + 1, deceit, war)
