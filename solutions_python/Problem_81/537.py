#!/usr/bin/env python3

T = int(input())

def get_wp(L, n, nots):
    count = 0.0
    wins = 0.0
    for j in range(len(L[n])):
        if j not in nots:
            if L[n][j] == '1':
                count += 1.0
                wins += 1.0
            elif L[n][j] == '0':
                count += 1.0

#    print('wp ', n, nots, '=', wins/count)
    return wins/count

def opponents(L, n):
    return filter(lambda i: L[n][i] in ['0', '1'], range(len(L[n])))

def get_owp_oowp(L, n):
    OPS = list(opponents(L, n))
    owp = 0.0
    oowp = 0.0

    for i in OPS:
        owp += get_wp(L, i, [n])/len(OPS)
        inOPS = list(opponents(L, i))

        inoowp = 0.0
        for j in inOPS:
            inoowp += get_wp(L, j, [i])/len(inOPS)

        oowp += inoowp / len(OPS)

    return owp, oowp

for case in range(T):
    N = int(input())
    L = [input() for n in range(N)]

    print('Case #{0}:'.format(case + 1))
    for i in range(len(L)):
        wp = get_wp(L, i, ())
        owp, oowp = get_owp_oowp(L, i)

#        print(wp, owp, oowp)
        print(0.25 * wp + 0.5 * owp + 0.25 * oowp)
