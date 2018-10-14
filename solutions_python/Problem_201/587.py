# coding: utf8
# Copyright: MathDecision

from collections import Counter
import numpy as np

def div(r):
    if r % 2 == 1:
        return r / 2, r / 2
    else:
        return r / 2, r / 2 - 1


def step(cont, keys, max_key):
    cont[max_key] -= 1
    k1, k2 = div(max_key)
    cont[k1] += 1
    cont[k2] += 1
    keys.add(k1)
    keys.add(k2)
    if cont[max_key] == 0:
        keys.remove(max_key)
        max_key = max(keys)
    return cont, keys, max_key, k1, k2


def proceed(N, k):
    cont = Counter({N: 1})
    keys = {N}
    max_key = N
    for i in range(k):
        cont, keys, max_key, k1, k2 = step(cont, keys, max_key)
    return k1, k2


def proceed_large(N, k):
    s = N
    n1 = 0
    n2 = 1
    t = 0
    return _proceed_large(s, n1, n2, t, k)

def _proceed_large(s, n1, n2, t, k):
    # print s, n1, n2, t, k
    if k <= 2**t:
        if k <= n1:
            return div(s + 1)
        else:
            return div(s)
    else:
        if s % 2 == 1:
            nn1 = n1
            nn2 = n1 + 2 * n2
        else:
            nn1 = 2 * n1 + n2
            nn2 = n2
        return _proceed_large((s - 1) / 2, nn1, nn2, t + 1, k - 2**t)


# def calculo(N, k):
#     t = int(np.log2(k)) - 1
#     kapp = (2**(t + 1) - 1)
#     kres = k - kapp
#     N1 = N - kapp
#     blocksize = N1 / 2**(t + 1)
#     ns1 = N1 / blocksize
#     ns2 = N1 - ns1 * blocksize



if __name__ == '__main__':
    #
    # N = 999
    # k = 255
    # proceed_large(N, k)
    # exit()
    #

    fi = 3
    responses = []
    inf = 'stalls{}.in'.format(fi)
    outf = 'stalls{}.out'.format(fi)
    with open(inf, 'r') as f:
        cases = int(f.readline())
        for i in range(cases):
            N, k = map(lambda x: int(x), f.readline().split(' '))
            #print N, k, proceed(N, k), proceed_large(N, k)
            #assert proceed(N, k) == proceed_large(N, k)
            responses.append(proceed_large(N, k))
    with open(outf, 'w') as f:
        for i, (r, l) in enumerate(responses):
            f.write('Case #{}: {} {}\n'.format(i + 1, r, l))
    #
    #
    # N = 1000
    # k = 1
    # print proceed(N, k)
