#! coding: utf-8
from math import log
from collections import Counter

if __name__ == '__main__':

    #python2:
    T = int(raw_input())
    for i in xrange(T):
        N, K = [int(s) for s in raw_input().split(" ")]

        l = int(log(K, 2))
        stalls = Counter({N:1})
        for j in xrange(l):
            new_stalls = Counter()
            for k in stalls:
                new_stalls[(k - 1) / 2] += stalls[k]
                new_stalls[k / 2] += stalls[k]
            stalls = new_stalls

        K -= 2 ** l - 1
        if K > stalls[sorted(stalls, reverse = True)[0]]:
            m = sorted(stalls, reverse = True)[-1]
        else:
            m = sorted(stalls, reverse = True)[0]
        l = (m - 1) / 2
        r = m / 2

        print("Case #{0}: {1} {2}".format(i + 1, r, l))
