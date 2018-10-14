#!/usr/bin/env python


def solve(n, a):
    f = {}
    for i, num in enumerate(sorted(a)):
        f[num] = i + 1
    for i in xrange(n):
        a[i] = f[a[i]]
    m = a.index(n)
    best_n_swaps = n * n
    for p in xrange(0, n):
        n_swaps = abs(m - p)
        b = a[:]
        del b[m]
        b.insert(p, n)
        for next_num in xrange(n - 1, 0, -1):
            j = b.index(next_num)
            if j < p:
                while b[j + 1] < next_num:
                    b[j], b[j + 1] = b[j + 1], b[j]
                    j += 1
                    n_swaps += 1
            else:
                while b[j - 1] < next_num:
                    b[j], b[j - 1] = b[j - 1], b[j]
                    j -= 1
                    n_swaps += 1
        if n_swaps < best_n_swaps:
            best_n_swaps = n_swaps
        assert sorted(b[:p]) == b[:p]
        assert sorted(b[p:], reverse=True) == b[p:]
    return best_n_swaps


def solve_take_two(n, a):
    f = {}
    for i, num in enumerate(sorted(a)):
        f[num] = i + 1
    for i in xrange(n):
        a[i] = f[a[i]]
    l = 0
    r = 0
    n_swaps = 0
    for next_num in xrange(1, n + 1):
        i = a.index(next_num)
        l_swaps = i - l
        r_swaps = n - 1 - r - i
        del a[i]
        if l_swaps < r_swaps:
            n_swaps += l_swaps
            a.insert(l, next_num)
            l += 1
        else:
            n_swaps += r_swaps
            a.insert(n - 1 - r, next_num)
            r += 1
    return n_swaps


def main():
    n_tests = int(raw_input())
    for test in xrange(1, n_tests + 1):
        n = int(raw_input())
        a = map(int, raw_input().split())
        print 'Case #%d: %d' % (test, solve_take_two(n, a))


if __name__ == '__main__':
    main()
