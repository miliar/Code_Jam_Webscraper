import sys

def nextRide(pos, g, maxMoney):
    newPos = pos
    money = 0
    cntG = 0
    while (cntG < len(g)) and (g[newPos] + money <= maxMoney):
        money += g[newPos]
        newPos = (newPos + 1) % len(g)
        cntG += 1
    
    return newPos, money

f = open(sys.argv[1])
tst = int(f.readline())
for t in xrange(0, tst):
    ar = f.readline().split()
    r = long(ar[0])
    k = long(ar[1])
    n = long(ar[2])

    g = []
    pos = []
    mon = []

    for s in f.readline().split():
        g.append(long(s))
        pos.append(-1)
        mon.append(long("-1"))

    curPos = 0
    ride = 0
    money = 0
    cicleReached = False
    while ride < r:
        if (pos[curPos] != -1) and not cicleReached:
            clen = ride - pos[curPos]
            wcicle = money - mon[curPos]
            kcicle = (r - ride) / clen
            money += wcicle * kcicle
            ride += kcicle * clen
            cicleReached = True


        if ride < r:
            pos[curPos] = ride
            mon[curPos] = money
            
            nextPos, curMon = nextRide(curPos, g, k)

            money += curMon
            curPos = nextPos
            ride += 1

    print "Case #" + str(t + 1) + ":", money
       