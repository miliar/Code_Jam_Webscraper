from itertools import combinations
from math import pi
from heapq import *


def prikazi(indeks, niz):
    return "Case #{}: {}".format(indeks, niz)



def resitev(stevci, P):
    zadovolni = 0
    ostanek = 0
    zadovolni += stevci[0]
    if P == 3:
        m = min(stevci[1:])
        M = max(stevci[1:])
        zadovolni += m
        ostane = M - m
        zadovolni += ostane // P + (1 if ostane % P > 0 else 0)
    elif P == 2:
        zadovolni += stevci[-1] // P + (1 if stevci[-1] % P > 0 else 0)
    else:
        assert P == 4
        return -1
    return zadovolni



def resi(ime):
    notr = ime + ".in"
    ven = ime + ".out"
    with open(notr) as f:
        with open(ven, "w") as ggg:
            for ind in range(int(f.readline())):
                N, P = [int(x) for x in f.readline().strip().split()]
                gs = tuple([(int(x) % P) for x in f.readline().strip().split()])
                stevci = [0 for _ in range(P)]
                for g in gs:
                    stevci[g] += 1
                print(prikazi(ind + 1, resitev(stevci, P)), file=ggg)

resi("A-small-attempt0")