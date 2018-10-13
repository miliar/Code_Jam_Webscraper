#!/usr/local/bin/pypy
# run with PyPy 2.6.1

def read_strings():
    return raw_input().strip().split(' ')

def read_ints():
    return [int(x) for x in read_strings()]

def count(g, p):
    ans = [0] * p
    for x in g:
        ans[x % p] += 1
    return ans

def f(rest, delta, sav):
    if sum(rest) == 0:
        return 0
    if (tuple(rest), delta) in sav:
        return sav[(tuple(rest), delta)]
    ans = 1 if delta == 0 else 0
    best = 0
    p = len(rest)
    for i in xrange(p):
        if rest[i] > 0:
            rest[i] -= 1
            best = max(best, f(rest, (delta + i) % p, sav))
            rest[i] += 1
    sav[(tuple(rest), delta)] = ans + best
    return ans + best

test_count, = read_ints()
for test in xrange(1, test_count + 1):
    n, p = read_ints()
    g = read_ints()

    start = count(g, p)
    ans = f(start, 0, {})

    print 'Case #{}: {}'.format(test, ans)
