# coding: utf-8

import bisect

def palindromes():
    for i in range(10) + range(11, 100, 11):
        yield i
    for d in xrange(1, 7):
        for i in xrange(10 ** d, 10 ** (d + 1)):
            yield i * 10**d + long(str(i)[::-1]) % (10 ** d)
        for i in xrange(10 ** d, 10 ** (d + 1)):
            yield i * 10**(d + 1) + long(str(i)[::-1])

def check(n):
    return str(n) == str(n)[::-1]

def main():
    v = [i * i for i in palindromes() if check(i * i)]
    N = int(raw_input())
    for tc in xrange(1, N + 1):
        A, B = map(long, raw_input().split())
        print 'Case #%d: %d' % (tc, bisect.bisect_right(v, B) - bisect.bisect_left(v, A))

if __name__ == '__main__':
    main()
