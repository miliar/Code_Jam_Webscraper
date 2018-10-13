def case():
    n = int(input())

    naomi = list(sorted(map(float, input().split())))
    ken = list(sorted(map(float, input().split())))

    # Regular war
    points = 0
    nj = n-1
    ki, kj = 0, n-1
    while nj >= 0:
        if naomi[nj] > ken[kj]:
            points += 1
            ki += 1
        else:
            kj -= 1
        nj -= 1

    # Deceitful war
    ni, nj = 0, n-1
    ki, kj = 0, n-1
    dpoints = 0
    while ni <= nj:
        if naomi[nj] > ken[kj]:
            dpoints += 1
            nj -= 1
            kj -= 1
        else:
            ni += 1
            kj -= 1

    return (dpoints, points)

ncases = int(input())
for i in range(ncases):
    p, d = case()
    print('Case #%d: %d %d' % (i+1, p, d))
