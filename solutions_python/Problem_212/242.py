t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, P = [int(s) for s in raw_input().split(" ")]
    G = [int(s) for s in raw_input().split(" ")]

    good = []
    notgood = []
    for g in G:
        if g % P == 0:
            good.append(g)
        else:
            notgood.append(g)

    # print good, notgood

    n1 = len(good)
    n2 = 0
    if notgood:
        if P == 2:
            n2 = (len(notgood) + 1) / 2
        else:
            for j,g in enumerate(notgood):
                notgood[j] = g % P
            if P == 3:
                a1 = notgood.count(1)
                a2 = notgood.count(2)
                if a1 < a2:
                    n2 = a1 + (a2 - a1 + 2) / P
                elif a1 == a2:
                    n2 = a1
                else:
                    n2 = a2 + (a1-a2 + 2) / P

    n = n1 + n2

    print "Case #{}: {}".format(i, n)

