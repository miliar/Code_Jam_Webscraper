def solve():
    N = raw_input()
    Naomi = map(float, raw_input().split(" "))
    Ken = map(float, raw_input().split(" "))

    Naomi.sort()
    Ken.sort()

    NaomiTmp = list(Naomi)
    KenTmp = list(Ken)

    y = 0
    z = 0

    while len(Naomi) > 0:
        if Naomi[0] <= Ken[0]:
            Naomi.pop(0)
            Ken.pop(- 1)
        else:
            tmp = Naomi.pop(0)
            Ken.pop(0)
            y += 1


    Naomi = NaomiTmp
    Ken = KenTmp

    while len(Naomi) > 0:
        tmp = Naomi.pop(0)
        for i, k in enumerate(Ken):
            if tmp < k:
                Ken.pop(i)
                break
        else:
            Ken.pop(0)
            z += 1


    return "%d %d" % (y, z)


T = int(raw_input())
for t in xrange(1, T + 1):
    print "Case #%d: %s" % (t, solve())
