def rec(n, base, state, lim, leading_zero):
    res = 0
    if not leading_zero and n * n <= lim or \
           leading_zero and base * base <= 10000 * lim:
        if not leading_zero:
            res += 1

        for d in [0, 1, 2]:
            next_state = 2 * d * d + state
            if next_state < 10:
                res += rec(n * 10 + d + d * base,
                           base * 100, next_state, lim, d == 0)
    return res


def solve(lim):
    res = rec(0, 10, 0, lim, True)
    for d in [0, 1, 2, 3]:
        res += rec(d, 100, d * d, lim, d == 0)
    return res


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        lo, hi = [int(k) for k in input().split()]
        res = solve(hi) - solve(lo - 1)
        print('Case #{}: {}'.format(t + 1, res))
