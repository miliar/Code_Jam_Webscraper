from itertools import combinations
from math import pi
from heapq import *

def prikazi(indeks, niz):
    return "Case #{}: {}".format(indeks, niz)


def pomo(sez):
    if sez[-1][1] - sez[0][0] <= 12 * 60:
        return 2
    elif sez[0][1] + (24 * 60 - sez[-1][0]) <= 12 * 60:
        return 2
    else:
        return 4


def resitevStaro(opra, ac, aj):
    if ac + aj == 1:
        return 2
    if not ac + aj == 2:
        return "NE VEM"
    if ac == 0:
        return pomo(opra[1])
    elif aj == 0:
        return pomo(opra[0])
    else:
        return 2

def dobiOpis(elt):
    interval, kdo = elt
    od, do = interval
    return kdo, od, do


def najdiNasl(slo, i, maxsi):
    for j in range(i + 1, maxsi):
        if j in slo:
            return j
    return 0


def resitev(opra):
    kajPopravil = True
    N = len(opra)
    kolko = [0, 0]
    slo = {}
    idOpra = 0
    for par in opra:
        kdo, od, do = dobiOpis(par)
        kolko[kdo] += do - od
        slo[idOpra] = ((od, do), kdo)
        idOpra += 1

    pavze = [[], []]
    for i in slo:
        kdo, od, do = dobiOpis(opra[i])
        kdoPol, odPol, doPol = dobiOpis(opra[(i + 1) % N])
        if kdo == kdoPol:
            pavza = odPol - do if i < N - 1 else (24 * 60 - do) + odPol
            heappush(pavze[kdo], (pavza, i, najdiNasl(slo, i, N)))

    while kajPopravil:
        kajPopravil = False
        for oseba in range(2):
            if pavze[oseba]:
                if pavze[oseba][0][0] + kolko[oseba] <= 720:
                    kolk, id1, id2 = heappop(pavze[oseba])
                    kolko[oseba] += kolk
                    _, od1, do1 = dobiOpis(slo[id1])
                    _, od2, do2 = dobiOpis(slo[id2])
                    if id2 != 0:
                        # del slo[id1]
                        # del slo[id2]
                        slo[id1] = ((od1, od2), oseba)
                    else:
                        slo[id1] = ((od1, 24 * 60), oseba)
                        slo[id2] = ((0, do2), oseba)
                    kajPopravil = True
            if kajPopravil:
                break
    menjave = 0
    for i in range(N):
        kdo1, od1, do1 = dobiOpis(slo[i])
        kdo2, od2, do2 = dobiOpis(slo[(i + 1) % N])
        if kdo1 != kdo2:
            menjave += 1
        elif ((do1 - od2) % (24 * 60)) != 0:
            menjave += 2
    return menjave


def resi(ime):
    notr = ime + ".in"
    ven = ime + ".out"
    with open(notr) as f:
        with open(ven, "w") as g:
            for ind in range(int(f.readline())):
                AC, AJ = [int(x) for x in f.readline().strip().split()]
                opravila = []
                for i in range(AC + AJ):
                    kdo = i < AC
                    interval = tuple([int(x) for x in f.readline().strip().split()])
                    opravila.append((interval, 1 - kdo))
                opravila.sort()
                print(prikazi(ind + 1, resitev(opravila)), file=g)

resi("B-large")