T = int(raw_input())

for i in range(T) :
    f = [int(k) for k in raw_input().split(' ')]
    N = f[0]
    S = f[1]
    p = f[2]
    t = f[3:]
    total = 0
    tosur = 0
    for r in t :
        if r % 3 == 0 :
            m = r / 3
        else :
            m = r / 3 + 1

        if p == 1 :
            lim = 1
        elif p == 2 :
            lim = 2
        else :
            lim = p + (p-2) + (p-2)

        if m >= p :
            total += 1
        elif r >= lim and m == p - 1 :
            tosur += 1
    total += min(tosur, S)
    print "Case #%d:" % (i + 1), total
