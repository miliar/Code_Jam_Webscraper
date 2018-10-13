import sys
import copy


def d_move(n, k):
    chosen = min(n)
    if min(n) > min(k):
        told = max(k) + 1
    else:
        told = max(k) - 0.0000001
    n.remove(chosen)
    return told, n, k


def w_move(n, k):
    chosen = max(n)
    n.remove(chosen)
    return chosen, n, k


def ken_move(told, n, k, pn):
    pos = [x for x in k if x > told]
    if len(pos) > 0:
        chosen = min(pos)
    else:
        chosen = min(k)
        pn += 1
    k.remove(chosen)
    return n, k, pn


def test():
    n = int(raw_input())
    naomi = [float(x) for x in raw_input().split()]
    ken = [float(x) for x in raw_input().split()]

    n1 = copy.deepcopy(naomi)
    k1 = copy.deepcopy(ken)
    pn1 = 0
    for i in range(0, n):
        told, n1, k1 = d_move(n1, k1)
        n1, k1, pn1 = ken_move(told, n1, k1, pn1)

    n1 = copy.deepcopy(naomi)
    k1 = copy.deepcopy(ken)
    pn2 = 0
    for i in range(0, n):
        told, n1, k1 = w_move(n1, k1)
        n1, k1, pn2 = ken_move(told, n1, k1, pn2)

    return pn1, pn2


def main():
    t = int(raw_input())
    for i in range(1, t + 1):
        y, z = test()
        print "Case #%d: %d %d" % (i, y, z)


main()