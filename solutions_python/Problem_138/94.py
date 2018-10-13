import copy

def war(naomi_, ken_):
    naomi = copy.deepcopy(naomi_)
    ken = copy.deepcopy(ken_)
    naomi.sort()
    ken.sort()
    nsc = 0
    ksc = 0
    for n in naomi:
        kch = -1
        for i, k in enumerate(ken):
            if k < n: continue
            kch = k
            ken[i] = -1
            break
        if kch >= 0:
            ksc += 1
        else:
            nsc += 1

    return nsc

def deceitful_war(naomi_, ken_):
    naomi = copy.deepcopy(naomi_)
    ken = copy.deepcopy(ken_)
    naomi.sort()
    ken.sort()

    n = len(naomi)
    for t in range(n):
        w = 0
        for i in range(n):
            if naomi[i] > ken[i]: w += 1
        if w == n:
            return w
        naomi = naomi[1:]
        ken = ken[:-1]
        n -= 1

    return 0

def main():
    T = input()
    for t in range(T):
        N = input()
        naomi = map(float, raw_input().split(' '))
        ken   = map(float, raw_input().split(' '))
        # print naomi, ken
        w = war(naomi, ken)
        dw = deceitful_war(naomi, ken)
        print "Case #%d: %d %d" % (1+t, dw, w)

if __name__ == '__main__':
    main()
