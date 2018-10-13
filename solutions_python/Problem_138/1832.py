T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    naomi = set([float(x) for x in raw_input().split()])
    ken = set([float(x) for x in raw_input().split()])
    naomi2 = naomi.copy()
    ken2 = ken.copy()
    fairCount = 0
    for i in range(N):
        if max(naomi) > max(ken):
            ken.remove(min(ken))
            naomi.remove(max(naomi))
            fairCount+=1
        else:
            ken.remove(max(ken))
            naomi.remove(max(naomi))
    naomi = naomi2
    ken = ken2
    cheatCount = 0
    for i in range(N):
        if min(naomi) > min(ken):
            ken.remove(min(ken))
            naomi.remove(min(naomi))
            cheatCount += 1
        else:
            ken.remove(max(ken))
            naomi.remove(min(naomi))
    print "Case #{}: {} {}".format(t, cheatCount, fairCount)
