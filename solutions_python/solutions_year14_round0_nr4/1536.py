#!/usr/bin/env python3
# coding: utf-8

from bisect import bisect_right

def dec(naos, kens):
    ret = 0

    for nao in naos:
        ken_min = min(kens)

        if nao < ken_min:
            kens.remove(max(kens))
        else:
            kens.remove(ken_min)
            ret += 1

    return ret

def war(naos, kens):
    ret = 0

    for nao in naos:
        i = bisect_right(kens, nao)

        if i == len(kens):
            i -= 1

        if nao < kens[i]:
            kens.remove(kens[i])
        else:
            kens.remove(min(kens))
            ret += 1

    return ret

for case in range(int(input())):
    n = int(input())
    naos = list(map(float, input().split(' ')))
    kens = list(map(float, input().split(' ')))

    naos.sort()
    kens.sort()

    print('Case #{}: {} {}'.format(
        case + 1, dec(naos[:], kens[:]), war(naos[:], kens[:])))
