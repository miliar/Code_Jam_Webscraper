#!/usr/bin/python3

import sys

def brute_force(n, k):
    L = [False for i in range(n)]
    L[0] = True
    L[-1] = True

    for i in range(k):
        best = (-1, -1, -1)
        for j in range(1 , n - 1):
            if L[j] == False:
                k = j
                cntLeft = 0
                while L[k] == False:
                    k -= 1
                    cntLeft += 1
                cntLeft -= 1

                k = j
                cntRight = 0
                while L[k] == False:
                    k += 1
                    cntRight += 1
                cntRight -= 1
                a = min(cntLeft, cntRight)
                b = max(cntLeft, cntRight)
                if (a, b) > best[:-1]:
                    best = (a, b, j)
        L[best[2]] = True
    return best[:-1]
def solve():
    T = int(input())
    for t in range(T):
        n, k = tuple(map(int, input().split()))
        a, b = fast(n, k)
        print('Case #{}: {} {}'.format(t + 1, b, a))

def pr(ls):
    for l in ls:
        print(' '.join(map(str, l)))

def biggest_power_smaller_than(base, k):
    exponent = 0
    value = 1
    while value <= k:
        exponent += 1
        value *= 2
    return exponent - 1

def split(x):
    return (x // 2 - 1, x // 2) if x % 2 == 0 else (x // 2, x // 2)

def fast(n, k):
    row = biggest_power_smaller_than(2, k)
    root = (n - 2 ** row) // (2 ** row)
    if k - 2 ** row <= n % (2 ** row):
        root += 1
    return split(root)

def test(maxn):
    tests = 0
    failed = 0
    fails = set()
    for n in range(maxn):
        for k in range(1, n + 1):
            tests += 1
            a_mine, b_mine = fast(n, k)
            a_corr, b_corr = brute_force(n + 2, k)
            if a_mine != a_corr or b_mine != b_corr:
                failed += 1
                set.add((n, k))
            if tests % 100 == 0:
                print('ran {} / {} tests, {} failed'.format(tests, maxn * (maxn - 1) // 2, failed))
    print('ran {} / {} tests, {} failed'.format(tests, maxn * (maxn - 1) // 2, failed))
    if failed > 0:
        print('fails: {}'.format(fails))

if __name__ == "__main__":
    if len(sys.argv) >=2:
        if sys.argv[1] == 'test':
            if len(sys.argv) >=3:
                test(int(sys.argv[2]))
        elif sys.argv[1] == 'run':
            solve()
