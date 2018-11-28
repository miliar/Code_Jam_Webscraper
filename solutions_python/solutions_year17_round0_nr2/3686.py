import functools
import random
import sys

files = ['B-sample', 'B-small-attempt0.in', 'B-large.in']
fn = files[2]


def naive(N):
    last = 0
    for i in range(N, 0, -1):
        if tidy(i):
            last = i
            return last

def less_naive(N):
    s = str(N)
    while not tidy(int(s)):
        # search for the first offender
        idx = -1
        for i in range(0, len(s)-1):
            if s[i] > s[i+1]:
                idx = i
                break

        s = s[:idx] + chr(ord(s[idx])-1) + '9'*(len(s)-idx-1)

    return int(s)


def tidy(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False

    return True

with open(fn) as f, open(fn + '.sol', 'wt') as sol:
    T = int(next(f))

    for t in range(1, T+1):
        N = int(next(f))

        print(N)
        last = less_naive(N)
        # last = naive(N)

        print('Case #{}: {}'.format(t, last))
        sol.write('Case #{}: {}\n'.format(t, last))
