T = input()

for casenbr in range(T):
    N = input()
    naomi = [float(i) for i in raw_input().strip().split()]
    ken = [float(i) for i in raw_input().strip().split()]

    naomi.sort()
    ken.sort()
    fair_wins = 0
    kplay = ken[:]
    for b in naomi:
        for b2 in kplay:
            if b2 > b:
                kplay.remove(b2)
                break
        else:
            fair_wins += 1
            kplay.pop(0)

    deceitful_wins = 0
    for idx in range(N):
        losers = [b1 for b1,b2 in zip(naomi,ken) if b1 < b2]
        if not losers:
            deceitful_wins = len(naomi)
            break
        naomi.remove(losers[0])
        ken.pop()

    print "Case #%d: %d %d" % (casenbr+1, deceitful_wins, fair_wins)
