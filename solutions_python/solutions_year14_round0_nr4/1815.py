__author__ = 'Adrian'


from decimal import Decimal


T = int(raw_input())

for test in range(T):
    N = int(raw_input())
    naomi = sorted([Decimal(x) for x in raw_input().split()])
    ken = sorted([Decimal(x) for x in raw_input().split()])
    #print [str(x) for x in naomi]
    #print [str(x) for x in ken]
    naomi_c = [x for x in naomi]
    ken_c = [x for x in ken]

    score_cheating, score = 0, 0

    while len(naomi) > 0:
        worst_ken = ken.pop()
        best_naomi = -1
        for i in range(len(naomi)):
            if naomi[i] > worst_ken:
                best_naomi = i
                break
        if best_naomi == -1:
            naomi.pop(0)
        else:
            naomi.pop(best_naomi)
            score_cheating += 1



    while len(naomi_c) > 0:
        worst_naomi = naomi_c.pop()
        best_ken = -1
        for i in range(len(ken_c)):
            if ken_c[i] > worst_naomi:
                best_ken = i
                break
        if best_ken == -1:
            ken_c.pop(0)
            score += 1
        else:
            ken_c.pop(best_ken)

    print 'Case #%d: %d %d' % (test + 1, score_cheating, score)

