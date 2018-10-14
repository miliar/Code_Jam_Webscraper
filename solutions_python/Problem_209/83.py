from itertools import combinations
from math import pi


def prikazi(indeks, niz):
    return "Case #{}: {}".format(indeks, niz)


def ploscina(palas):
    plasc = sum(2 * r * pi * h for (r, h) in palas)
    return plasc + pi * palas[0][0]**2


def resitev(palas, N, K):
    maxS = 0
    palas.sort(key=lambda x: x[0] * x[1], reverse=True)
    for i, pala in enumerate(palas):
        moznosti = [pala]
        k = 0

        while k < N and len(moznosti) < K:
            if k != i and palas[k][0] <= moznosti[0][0]:
                moznosti.append(palas[k])
            k += 1
        if len(moznosti) == K:
            maxS = max(maxS, ploscina(moznosti))
    return maxS



def resi(ime):
    notr = ime + ".in"
    ven = ime + ".out"
    with open(notr) as f:
        with open(ven, "w") as g:
            for ind in range(int(f.readline())):
                N, K = [int(x) for x in f.readline().strip().split()]
                pala = []
                for i in range(N):
                    r, h = [int(x) for x in f.readline().strip().split()]
                    pala.append((r, h))
                print(prikazi(ind + 1, resitev(pala, N, K)), file=g)

resi("A-large")