# codejam
from sys import stdin


def longest(a):
    max_len = 0
    max_idx = len(a)
    c_len = 0

    for i in range(len(a) - 1, -2, -1):
        if (i >= 0 and a[i] == 0):
            c_len += 1
        else:
            if c_len >= max_len:
                max_len = c_len
                max_idx = i + 1
            c_len = 0

    return max_len, max_idx


def flip(a, start, length):
    for i in range(start, start + length):
        if a[i] == 0:
            a[i] = 1
        else:
            a[i] = 0


# Solver
def solve(S, K):
    a = []
    for c in S:
        if c == '-':
            a.append(0)
        else:
            a.append(1)

    for i in range(0, len(S) * 10):
        ml, mli = longest(a)
        if ml == 0:
            return i

        if mli + K > len(S):
            mli = len(S) - K

        flip(a, mli, K)

    return 'IMPOSSIBLE'

# I/O
T = int(stdin.readline())

for t in range(0, T):
    S, K = stdin.readline().split(' ')
    K = int(K)
    print('Case #{0}: {1}'.format(t + 1, solve(S, K)))
