#!/usr/local/bin/pypy
# run with PyPy 2.6.1

def read_strings():
    return raw_input().strip().split(' ')

def read_ints():
    return [int(x) for x in read_strings()]

def last_tidy(n):
    k = len(str(n))
    min_tidy = int('1' * k)
    if min_tidy > n:
        return '9' * (k - 1)
    ans = ''
    last_digit = 1
    for i in xrange(k):
        good = None
        for d in xrange(last_digit, 10):
            cand = int(ans + str(d) * (k - i))
            if cand > n:
                break
            else:
                good = d
        last_digit = good
        ans += str(good)
    return ans

test_count, = read_ints()
for test in xrange(1, test_count + 1):
    n, = read_ints()
    print 'Case #{}: {}'.format(test, last_tidy(n))
