# QR 2017
from sys import stdin, stdout, stderr, setrecursionlimit

setrecursionlimit(150000)


def solve(S, K):
    flips = 0
    target = '-'

    it = iter(S)
    i = 0
    while True:
        try:
            s = next(it)
            if s == target:
                if i + K - 1 >= len(S):
                    return 'IMPOSSIBLE'
                flips += 1
                it = flip_first_k(it, K - 1)
        except StopIteration:
            break
        else:
            i += 1

    return flips


def flip_first_k(iterable, k):
    count = 0
    for i in iterable:
        if count < k:
            count += 1
            yield flip(i)
        else:
            yield i


def flip(t):
    return '+' if t == '-' else '-'


if __name__ == "__main__":
    cases = int(stdin.readline())
    for c in range(1, cases + 1):
        S, K = stdin.readline().split()
        ans = solve(S, int(K))
        stdout.write("Case #{0}: {1}\n".format(c, ans))
