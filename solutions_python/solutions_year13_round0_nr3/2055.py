def pal(i):
    s = str(i)
    return s == s[::-1]

z = int(raw_input())
for _i in xrange(z):
    A, B = map(int, raw_input().split())
    a = int(A ** 0.5)
    b = int(B ** 0.5) + 1
    c = 0
    for i in xrange(a, b + 1):
        if A <= i ** 2 <= B:
            if pal(i) and pal(i ** 2):
                c += 1
    print 'Case #%d: %d' % (_i + 1, c)
