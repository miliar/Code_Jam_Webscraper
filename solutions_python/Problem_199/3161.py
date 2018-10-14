# -*- coding: utf-8 -*-
import itertools as it

def flip(c):
    if c == '+':
        return '-'
    if c == '-':
        return '+'
    raise Exception('+か-ではない')

def flips(c, n):
    flipped = []
    for i in range(len(list(c)) - n + 1):
        list_c = list(c)
        for j in range(n):
            list_c[i + j] = flip(list(c)[i + j])
        flipped.append(''.join(list_c))
    return flipped

def seen(l):
    return [p[0] for p in l]

def all_n_plus_one(n, all, K):
    all_n = [r for r in all if r[1] == n]
    nexts = [flips(c[0], K) for c in all_n]
    not_seen = list(set([x for x in list(it.chain.from_iterable(nexts)) if x not in seen(all)]))
    if not not_seen:
        return all
    all += [(u, n + 1) for u in not_seen]
    return all_n_plus_one(n + 1, all, K)

def solve(x):
    Ss, K = x.split(' ')
    K = int(K)
    all_plus = '+' * len(Ss)
    all = [(all_plus, 0)]

    all_patterns = all_n_plus_one(0, all, K)
    if Ss in seen(all_patterns):
        return min([q[1] for q in all_patterns if q[0] == Ss])

    return 'IMPOSSIBLE'

for case in range(1, 1 + int(input())):
    xi = input()
    print('Case #{}: {}'.format(case, solve(xi)))
