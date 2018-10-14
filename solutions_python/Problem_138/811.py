#! /usr/bin/python
import sys

def kenTurn(told, blocks):
    for bk in blocks:
        if bk > told:
            return bk
    return blocks[-1]

def War(naomi, ken, n):
    naomi = sorted(naomi)
    ken = sorted(ken)

    naomiScore = 0
    kenScore = 0

    for i in range(n):
        naomiChosen = naomi.pop(0)
        kenChosen = kenTurn(naomiChosen, ken)
        ken.remove(kenChosen)
        if kenChosen > naomiChosen:
            kenScore += 1
        else:
            naomiScore += 1
    return naomiScore

def DeceitfulWar(naomi, ken, n):
    naomi = sorted(naomi)
    ken = sorted(ken)

    naomiScore = 0
    kenScore = 0
    for i in range(n):
        if max(naomi) > max(ken):
            naomiChosen = naomi.pop()
        else:
            naomiChosen = naomi.pop(0)
        naomiTell = naomiChosen
        maxken = max(ken) - 0.000001
        if maxken > naomiChosen:
            naomiTell = maxken
        kenChosen = kenTurn(naomiTell, ken)
        ken.remove(kenChosen)
        if kenChosen > naomiChosen:
            kenScore += 1
        else:
            naomiScore += 1
    return naomiScore

fh = open(sys.argv[1])

count = int(fh.readline())

for i in range(count):
    n = int(fh.readline())
    naomi = [float(c) for c in fh.readline().split()]
    ken = [float(c) for c in fh.readline().split()]

    print "Case #%d: %d %d" % (i + 1, DeceitfulWar(naomi, ken, n), War(naomi, ken, n))
