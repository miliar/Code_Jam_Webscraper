import string

def numbers(n):
    s = str(n)
    l = len(s)
    for i in xrange(1, l):
        ms = string.lstrip(s[-i:] + s[:-i], '0')
        m = int(ms)
        if len(ms) == l and m > n:
            yield m

def solve(A, B):
    pairs = set()
    for n in xrange(A, B + 1):
        for m in numbers(n):
            if m <= B:
                pairs.add((n, m))
    return len(pairs)

if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        A, B = (int(s) for s in raw_input().split())
        n = solve(A, B)
        print 'Case #%d: %d' % (i, n)
