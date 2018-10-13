import functools
import random
import sys

files = ['A-sample', 'A-small-attempt0.in', 'A-large-practice.in']
fn = files[1]


def flip(s, idx, flipsize):
    assert len(s) >= idx + flipsize
    flipped = ''.join(map(lambda c: '-' if c == '+' else '+', s[idx:idx+flipsize]))
    return s[:idx] + flipped + s[idx+flipsize:]


def done(s):
    return '-' not in s

# do a BFS from the all happy state to find all the solvable states
# and the optimal number of steps to reach them
def BFS_me_slowly(l, K, needle):
    seen = {'+'*l: 0}
    parent = {'+'*l: None}
    next = ['+'*l]
    level = 1
    if needle == next[0]:
        return 0, parent

    while next and level < l*15:
        nextnext = []
        for n in next:
            for i in range(0, l-K+1):
                flipped = flip(n, i, K)
                if flipped not in seen:
                    parent[flipped] = n
                    seen[flipped] = level
                    nextnext.append(flipped)
                if flipped == needle:
                    return level, parent

        next = nextnext
        level += 1

    return -1, parent


with open(fn) as f, open(fn + '.sol', 'wt') as sol:
    T = int(next(f))

    for t in range(1, T+1):
        S, K = next(f).split()
        K = int(K)

        print(S, K)
        opt, parent = BFS_me_slowly(len(S), K, S)
        print(opt)
        if opt != -1:
            n = S
            while parent[n]:
                print(n)
                n = parent[n]

        if opt == -1: opt = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(t, opt))
        sol.write('Case #{}: {}\n'.format(t, opt))
