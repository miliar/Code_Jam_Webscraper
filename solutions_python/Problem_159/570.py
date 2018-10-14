def mushroom(nplates):
    mushrooms = [int(i) for i in raw_input().strip().split(' ')]
    differences = [mushrooms[i-1] - mushrooms[i] for i in xrange(1,nplates)]
    strategy_1 = 0
    for i in differences:
        if i>0:
            strategy_1 += i
    rate = max(differences)
    strategy_2 = 0
    for i in xrange(nplates-1):
        strategy_2 += min(rate, mushrooms[i])
    return strategy_1, strategy_2

ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
    res = mushroom(int(raw_input().strip()))
    print "Case #{0}: {1} {2}".format(i, res[0], res[1])
